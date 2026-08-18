# 日本悖論 VI–X：多載體地位持續與載體轉換模型 v0.4

**系列**：日本悖論研究系列延伸  
**性質**：理論收斂／跨層整合模型／歷史研究設計  
**版本**：v0.4  
**狀態**：候選整合框架，不宣稱已完成新一般理論  
**前置文件**：
- `Japan_Paradox_VI-X_Historical_Case_Counterexample_Matrix_v0.1.md`
- `Japan_Paradox_VI-X_Theory_Interface_Falsifiability_v0.2.md`
- `Japan_Paradox_VI-X_Core_Mechanism_Audit_and_Pivot_v0.3.md`

---

# 0. 本輪轉折

v0.3 已確認：

$$
\text{second-order respect},
$$

$$
\text{self-reinforcing status},
$$

$$
\text{common-knowledge status},
$$

$$
\text{pluralistic ignorance}
$$

都已有成熟研究傳統。

本輪因此不再試圖把「地位回饋」本身當作新機制，而提出一個更接近原日本悖論 I–V 的問題：

$$
\boxed{
\text{What persists when the status carrier changes?}
}
$$

中文：

> **當承載地位的主體被替換時，什麼東西使地位仍能持續？**

這把日本悖論 V 的「連續性對象」問題與 VI–X 的「英雄／地位／再納入」問題真正接起來。

---

# 1. 身份連續性與地位連續性必須分開

日本悖論 V 處理：

$$
I(X_t,X_{t+1})
=
\text{identity continuity judgment}.
$$

但地位連續問題是另一個函數：

$$
T_{a\rightarrow b}^{(d)}
=
\text{status influence transmitted from carrier }a\text{ to }b
\text{ in domain }d.
$$

因此完全可能：

$$
I(a,b)=0
$$

但：

$$
T_{a\rightarrow b}^{(d)}>0.
$$

也就是：

> 兩個人明明不是「同一個人」，但前一個人的家名、職位、聲望、關係與制度資源仍會影響下一個人的地位。

反過來也可能：

$$
I(X_t,X_{t+1})\approx1
$$

但：

$$
S_X(t+1)\ll S_X(t).
$$

同一個人仍然是同一個人，卻可能失去地位。

所以：

$$
\boxed{
\text{Identity Persistence}
\neq
\text{Status Persistence}.
}
$$

---

# 2. 既有研究已經覆蓋「同載體自我強化」

Gould（2002）的正式模型已經指出：

> 行動者會依照集體已給出的地位歸因，調整自己對其他人的地位授予行為。

因此：

$$
\text{collective attribution}
\rightarrow
\text{individual status-conferring gesture}
\rightarrow
\text{aggregate attribution}
$$

可以形成：

$$
\boxed{
\text{self-reinforcing status ranking}.
}
$$

Magee 與 Galinsky（2008）也系統整理了權力與地位階序的自我強化性。

所以本文件不宣稱：

$$
\text{status feedback}
$$

是新發現。

---

# 3. 地位長期穩定不等於每一期都固定

Smith 與 Faris（2015）的 longitudinal network 研究非常重要。

他們發現：

$$
\text{short-run status mobility}>0,
$$

但：

$$
\text{long-run rank stability}
$$

仍可能很高。

原因不是每個人永遠動不了，而是：

$$
\boxed{
\text{past position exerts drag}.
}
$$

上升者常常不能維持新取得的地位，最後被拉回原有位置。

這告訴我們：

$$
\boxed{
\text{Persistence}
\neq
\text{Staticness}.
}
$$

真正需要研究的是：

$$
\rho
=
\text{status persistence coefficient}.
$$

而不是只看單一時點排名。

---

# 4. 第一個生態調節變量：關係穩定性與互惠結構

Smith 與 Faris 的結果顯示，地位移動能否持久受到網路結構調節。

這使 v0.3 的「遞迴地位生態」得到更具體的形式：

$$
\rho
=
F(
\text{tie persistence},
\text{reciprocity structure},
\text{exit cost},
\text{institutional hierarchy},
\ldots
).
$$

因此日本特殊性若存在，不應寫成：

$$
\text{Japanese psychology is unique}.
$$

而更適合測試：

$$
\boxed{
\text{some Japanese historical ecologies}
\rightarrow
\rho\uparrow.
}
$$

---

# 5. 地位可以由關聯外溢，但外溢是條件性的

Overton（2021）的實驗顯示：

$$
\text{associate status}
\rightarrow
\text{focal person's status}.
$$

亦即：

$$
T_{a\rightarrow b}>0
$$

確實可能。

但最重要的限制是：

> status-by-association 對 deference 的外溢，取決於前後情境所需要的能力是否相似。

所以：

$$
\boxed{
T_{a\rightarrow b}
\text{ is domain-specific}.
}
$$

不能假設一個人的軍事威望會自動轉成所有領域的道德、學術或政治正統。

因此正式改成：

$$
T_{a\rightarrow b}^{(d)}.
$$

---

# 6. 地位不是守恆量

本模型嚴格禁止把地位寫成物理守恆量。

不使用：

$$
S_a+S_b=\text{constant}.
$$

更適合的表示是：

$$
S_b^{(d)}(t+1)
=
G\left(
A_b,
Z_b,
\Phi_b,
\sum_a
T_{a\rightarrow b}^{(d)}
S_a^{(d)}(t),
\mathcal E_t
\right).
$$

其中：

- $A_b$：承載者自身屬性；
- $Z_b$：制度與關係位置；
- $\Phi_b$：當期他人承認／服從／評價；
- $T_{a\rightarrow b}^{(d)}$：來自其他載體的地位影響；
- $\mathcal E_t$：制度與社會生態。

每一期地位都必須被重新生成：

$$
\boxed{
\text{status is re-conferred, not conserved}.
}
$$

---

# 7. 候選框架：Multi-Carrier Status Persistence

暫定英文：

## Multi-Carrier Status Persistence

縮寫：

## MCSP

中文：

## 多載體地位持續

這不是宣稱既有文獻沒有 status spillover、status inheritance 或 reputation transfer，而是把它們整合成一個「連續性對象」式框架。

定義載體集合：

$$
\mathcal C
=
\{
P,H,O,G,N,R,E
\},
$$

其中：

- $P$：Person，個人；
- $H$：House / Lineage，家／家系；
- $O$：Office / Role，職位／角色；
- $G$：Group / Organization，團體／組織；
- $N$：Narrative，故事／傳記／共同記憶；
- $R$：Ritual / Symbol，祭祀／稱號／象徵；
- $E$：External Evaluator / Institution，法律、排名、國家承認等外部認證載體。

---

# 8. Status Carrier Transition Graph

定義有向圖：

$$
\mathcal G_S
=
(
\mathcal C,
\mathcal T
),
$$

其中每一條邊：

$$
a
\xrightarrow{
T_{a\rightarrow b}^{(d)}
}
b
$$

表示：

> 載體 $a$ 的既有地位，在領域 $d$ 中對載體 $b$ 的新地位生成具有可測量影響。

例如：

$$
P_{\text{father}}
\rightarrow
H
\rightarrow
P_{\text{heir}},
$$

或：

$$
P_{\text{hero}}
\rightarrow
N_{\text{story}}
\rightarrow
P_{\text{later audience model}}.
$$

以及：

$$
G_{\text{prestigious organization}}
\rightarrow
P_{\text{member}}.
$$

---

# 9. 日本「家」是極乾淨的載體替換案例

Tokugawa 武士研究顯示，養子制度主要不是讓低階武士向上流動，而是：

$$
\boxed{
\text{preserve samurai lineages}
+
\text{preserve hereditary political order}.
}
$$

Moore 的四藩資料指出，十八世紀部分藩的中上層武士家族每代仍有顯著消失率；若沒有養子補充繼承人，家系死亡率會大幅提高。

所以：

$$
P_{\text{old head}}
\rightarrow
H
\rightarrow
P_{\text{adopted heir}}
$$

不是單純：

$$
\text{biological inheritance}.
$$

而是一種：

$$
\boxed{
\text{carrier substitution}.
}
$$

---

# 10. 2026 年量化證據：養子不是只把家「撐住」，還可能提高精英持續率

Kumanomido 與 Takayasu（2026）利用 1903–1939 年 Personnel Inquiry Records 建立父親—繼承人連結資料。

最重要結果包括：

$$
P(\text{elite}\mid\text{adopted heir})
>
P(\text{elite}\mid\text{biological heir}).
$$

最終同行評審版本報告：

- 養子繼承人約高 **19%** 機率繼續維持精英身份；
- 約高 **31%** 機率進入收入最高 $0.1\%$ ；
- 樣本中的精英家平均代際持續率約為 $17\%$ ；
- 可追溯生父的小樣本中，約 $56.8\%$ 的精英養子來自未被 PIR 列為精英的家庭。

這提供一個非常重要的機制：

$$
\boxed{
\text{House Continuity}
+
\text{Successor Selection}
\rightarrow
\text{Elite Persistence}.
}
$$

也就是：

> 家的地位持續不只可能倚賴「把親生兒子放上去」，還可以透過替換更合適的個體承載者維持。

---

# 11. 「家」因此可以視為 Institutional Status Buffer

內部候選名稱：

## Institutional Status Buffer

中文：

## 制度性地位緩衝器

它不是保存一個固定地位數值，而是保存：

- 家名；
- 財產；
- 官職通道；
- 人脈；
- 家臣；
- 婚姻網；
- 教育資源；
- 象徵資本；
- 外部承認；
- 繼承規則。

因此當個人載體死亡時：

$$
P_t\rightarrow\varnothing,
$$

仍可能：

$$
H_t
\approx
H_{t+1}.
$$

再由：

$$
H_{t+1}
\rightarrow
P_{t+1}
$$

重新生成繼承人的地位。

---

# 12. 這正好區分「個人不死」與「節點不死」

日本悖論 II 原本已有：

$$
\boxed{
\text{Node turnover}
\neq
\text{Topology collapse}.
}
$$

現在可以再加：

$$
\boxed{
\text{Carrier turnover}
\neq
\text{Status-field collapse}.
}
$$

只要存在足夠的：

$$
T_{H\rightarrow P}^{(d)},
$$

就算：

$$
I(P_t,P_{t+1})=0,
$$

仍可能：

$$
S_{P_{t+1}}^{(d)}
\gg0.
$$

這就是原日本悖論與新地位理論目前最重要的橋。

---

# 13. Prestige bias 提供「為什麼大家會跟著大家看某人」的文化傳播機制

Henrich 與 Gil-White（2001）的 prestige theory 已指出：

> 人會利用其他人給予某個人的注意、尊敬與自願性服從，作為判斷誰值得學習的間接線索。

因此：

$$
\text{others defer to }x
\rightarrow
\text{I infer }x\text{ is a useful model}
\rightarrow
\text{I copy / attend to }x.
$$

這會形成：

$$
\boxed{
\text{copied because others copy}
}
$$

式的 rich-get-richer 動態。

所以「英雄節點被放大」的微觀基礎也不是空白。

---

# 14. Narrative 可以成為新的地位載體

Berl 等人（2021）的 narrative transmission 實驗顯示：

- storyteller prestige 對資訊記憶／傳播有可測量效果；
- 但 narrative content 本身往往比 prestige cue 更重要；
- prestige 與內容偏差可以同時作用。

因此英雄死後：

$$
P_{\text{hero}}
\rightarrow
N_{\text{hero story}}
$$

之後，故事本身可以成為新載體。

其動態可寫成：

$$
S_N(t+1)
=
G(
S_N(t),
C_N,
R_N,
\text{retelling},
\text{institutional endorsement}
),
$$

其中：

- $C_N$：content attractiveness；
- $R_N$：storyteller / source prestige。

所以：

$$
\boxed{
\text{person dies}
\not\Rightarrow
\text{status signal disappears}.
}
$$

---

# 15. 義經、西鄉、菅原道真型案例應重新分類

以前容易把它們全放進：

$$
\text{forgiveness}.
$$

現在應拆成：

### A. Material / Political Status

$$
S_{\text{political}}.
$$

### B. Narrative Status

$$
S_{\text{narrative}}.
$$

### C. Moral / Heroic Status

$$
S_{\text{heroic}}.
$$

### D. Ritual / Sacred Status

$$
S_{\text{ritual}}.
$$

所以某人可能：

$$
S_{\text{political}}\downarrow0
$$

同時：

$$
S_{\text{narrative}}\uparrow,
$$

甚至：

$$
S_{\text{ritual}}\uparrow.
$$

這不是地位「消失又復活」，而是：

$$
\boxed{
\text{status-domain migration}.
}
$$

---

# 16. 地位應改成向量，而不是單一數值

定義：

$$
\mathbf S_x
=
(
S_C,
S_A,
S_P,
S_D,
S_L,
S_N,
S_M,
S_R
),
$$

其中：

- $S_C$：competence；
- $S_A$：agency；
- $S_P$：prestige；
- $S_D$：dominance；
- $S_L$：legitimacy；
- $S_N$：narrative salience；
- $S_M$：moral / heroic status；
- $S_R$：ritual / sacred status。

因此戰敗者不必：

$$
\mathbf S_x
\rightarrow
\mathbf 0.
$$

更可能：

$$
S_L\downarrow,
\quad
S_D\downarrow,
$$

但：

$$
S_C\approx\text{high},
\quad
S_P>0,
\quad
S_N>0.
$$

---

# 17. 「敵人變同伴」因此可以重寫成 Status-Vector Rebinding

暫定內部概念：

## Status-Vector Rebinding

中文：

## 地位向量重新綁定

對戰敗敵人 $x$：

$$
\mathbf S_x^{\text{enemy}}
=
(
C,A,P,D,L,N,\ldots
).
$$

戰敗後：

$$
D\downarrow,
$$

$$
T_{\text{threat}}\downarrow.
$$

但如果：

$$
C,
P,
N
$$

仍高，新秩序可能把這些殘留維度重新綁定到新的制度角色：

$$
P_x^{\text{enemy}}
\rightarrow
O_x^{\text{new regime}}.
$$

所以：

$$
\boxed{
\text{reintegration}
\neq
\text{moral forgiveness}.
}
$$

更可能是：

$$
\boxed{
\text{retain valuable status dimensions}
+
\text{replace political binding}.
}
$$

這對榎本武揚型案例尤其適合。

---

# 18. 英雄與強敵因此可能共享同一個「高資訊價值節點」來源

Prestige theory 強調：

$$
\text{deference}
$$

可以作為：

$$
\text{model quality cue}.
$$

因此一個被多人承認的強敵即使政治上被擊敗，也可能仍具有：

$$
S_C\uparrow,
\quad
S_A\uparrow,
\quad
S_N\uparrow.
$$

如果新秩序能降低：

$$
S_{\text{threat}},
$$

則可能：

$$
P(\text{reintegration})\uparrow.
$$

這是 VIII 最值得保留的候選路徑之一。

---

# 19. 但「強敵吸收」仍不是日本特有

一般 political co-optation、rebel reintegration、elite inclusion 文獻已研究大量類似機制。

因此日本特殊性不能寫成：

$$
\text{Japan uniquely absorbs strong enemies}.
$$

真正可驗證的是：

$$
\boxed{
\text{Does a house/role/narrative continuity system increase }
T_{a\rightarrow b}^{(d)}
\text{ across political rupture?}
}
$$

這是一個比較制度問題。

---

# 20. 多載體冗餘假說

若一個人的地位只存在於：

$$
P,
$$

則個體死亡或失敗可能造成：

$$
S\downarrow\downarrow.
$$

若同時存在：

$$
P+H+O+G+N+R,
$$

則某一載體消失後，其他載體仍可能重新生成地位訊號。

定義載體冗餘：

$$
\mathcal R_S(x)
=
\left|
\left\{
c\in\mathcal C:
T_{x\rightarrow c}^{(d)}>0
\right\}
\right|.
$$

候選假說：

$$
\boxed{
\mathcal R_S\uparrow
\Rightarrow
\text{status persistence after shock}\uparrow.
}
$$

---

# 21. Status Bridge Hypothesis

若兩個個體沒有身份連續：

$$
I(P_a,P_b)=0,
$$

但共享：

- 同一個家；
- 同一個職位；
- 同一套祭祀；
- 同一個組織；
- 同一個故事；
- 同一個正統性路徑；

則可能：

$$
T_{a\rightarrow b}^{(d)}>0.
$$

稱為：

## Status Bridge

中文：

## 地位橋

在日本家制度中最乾淨的形式就是：

$$
P_a
\rightarrow
H
\rightarrow
P_b.
$$

---

# 22. Status Persistence Decomposition

地位持續可以至少拆成五種不同機制：

## M1｜Autocatalytic Conferral

$$
S_t
\rightarrow
\text{more deference}
\rightarrow
S_{t+1}.
$$

已有 Gould、Magee–Galinsky 等研究。

## M2｜Cumulative Advantage / Historical Drag

$$
S_t
\rightarrow
\text{future opportunity structure}
\rightarrow
S_{t+n}.
$$

已有 Matthew effect 與 status dynamics 文獻。

## M3｜Associative Spillover

$$
S_a
\rightarrow
S_b.
$$

已有 status-by-association 與組織 status spillover 文獻。

## M4｜Institutional Carrier Substitution

$$
P_a
\rightarrow
H/O
\rightarrow
P_b.
$$

日本養子、繼承與家制度是非常好的案例。

## M5｜Narrative / Symbolic Re-encoding

$$
P_a
\rightarrow
N/R
\rightarrow
S_{\text{future}}.
$$

英雄故事、祭祀、稱號、共同記憶屬此類。

---

# 23. 本輪最有可能保留的理論新增量

v0.4 不再追求：

$$
\text{new micro-psychological primitive}.
$$

而把可能的新增量放在：

$$
\boxed{
\text{cross-carrier continuity architecture}.
}
$$

也就是研究：

> 一個社會如何用不同載體，把地位從一個已經消失、失敗或被替換的主體，重新生成到下一個主體、角色、家系或敘事中。

---

# 24. 日本特殊性應改成「載體架構」問題

未來真正值得比較的不是：

> 日本人是否更崇拜強者？

而是：

$$
\boxed{
\mathcal G_{S,\mathrm{Japan}}
\stackrel{?}{\neq}
\mathcal G_{S,\mathrm{comparison}}.
}
$$

具體測試：

- 日本歷史上的 $P\rightarrow H$ 是否特別強？
- $H\rightarrow P_{\text{heir}}$ 是否有較低衰減？
- $P\rightarrow N$ 的英雄敘事是否具有特殊結構？
- $N\rightarrow R$ 的祭祀／制度化是否較容易？
- political defeat 後， $S_C$ 是否較容易被保留並重新綁定？
- 現代化後，這些轉換係數是否下降、轉換到公司／組織／品牌等新載體？

---

# 25. 一個真正可測試的歷史資料設計

對每一名歷史人物建立：

$$
\mathbf X_i
=
(
\mathbf S_i^{\text{before}},
\mathbf S_i^{\text{after}},
\mathcal C_i,
\mathcal T_i
).
$$

### 人物前狀態

- 官位；
- 家格；
- 軍事能力；
- 財產；
- 關係網；
- 敵方評價；
- 主君評價；
- 群眾／後世評價。

### 事件

- 戰敗；
- 流放；
- 改易；
- 收養；
- 改仕；
- 赦免；
- 任官；
- 死亡；
- 追贈；
- 神格化。

### 後狀態

分別量：

$$
S_C,S_P,S_D,S_L,S_N,S_M,S_R.
$$

這樣就能區分：

$$
\text{status annihilation}
$$

與：

$$
\text{status migration / rebinding}.
$$

---

# 26. VI–X 再次更新

## VI｜關係社會中的英雄節點

研究：

$$
P
\rightarrow
N
\rightarrow
\text{collective focal individual}.
$$

重點轉為英雄地位如何跨人物生命期持續。

## VII｜社會位階解析

研究：

$$
\mathbf S
$$

的多維判定，以及不同載體提供的地位訊號如何被加權。

## VIII｜敵人再納入

正式核心改成：

$$
\boxed{
\text{Status-Vector Rebinding}.
}
$$

## IX｜蠻橫強者與地位維持

研究：

$$
\text{self-reinforcing deference}
+
\text{institutional buffer}
+
\text{exit cost}.
$$

## X｜從集體主義到地位載體生態

最後整合：

$$
\boxed{
\text{Recursive Status Ecology}
+
\text{Multi-Carrier Status Persistence}.
}
$$

---

# 27. 三條新可否證假說

## H1｜Carrier Redundancy Hypothesis

$$
\mathcal R_S\uparrow
\Rightarrow
P(\text{status survives shock})\uparrow.
$$

如果多載體人物／家系在死亡、戰敗或制度變更後並沒有更高地位持續率，則此假說失敗。

## H2｜Institutional Substitution Hypothesis

在控制初始資源後：

$$
T_{H\rightarrow P_{\text{successor}}}
$$

較高的制度應有較高的：

$$
\text{intergenerational status persistence}.
$$

日本養子制度提供直接案例。

## H3｜Domain Migration Hypothesis

重大失敗後：

$$
S_{\text{political}}\downarrow
$$

不必導致：

$$
S_{\text{narrative}},
S_{\text{moral}},
S_{\text{ritual}}
$$

同步下降。

如果多數歷史案例呈現所有地位維度同步崩潰，則「地位域遷移」的重要性下降。

---

# 28. 一個值得保留的總命題

原日本悖論 V：

$$
\boxed{
\text{What must persist for an entity to remain the same entity?}
}
$$

現在新增：

$$
\boxed{
\text{What must persist for a social status to remain causally active?}
}
$$

兩者的答案不必相同。

因此：

$$
\boxed{
\text{Continuity of Being}
\neq
\text{Continuity of Social Effect}.
}
$$

這可能是目前日本悖論 I–X 最重要的一個理論接縫。

---

# 29. 下一輪研究方向

下一輪優先研究：

## A. Status-domain migration

找政治失敗後：

$$
S_{\text{political}}
\rightarrow
S_{\text{heroic/narrative}}
$$

的比較歷史案例。

## B. Institutional carrier substitution

擴充日本養子之外：

- 歐洲貴族收養／指定繼承；
- 中國宗族；
- 韓國宗家；
- 商號與家業；
- 宗教職位；
- 現代企業 succession。

## C. Enemy rebinding

建立：

$$
\text{defeated}
\rightarrow
\text{eliminated}
$$

與：

$$
\text{defeated}
\rightarrow
\text{reintegrated}
$$

配對資料。

---

# 30. 核心文獻錨點

1. Gould, R. V. (2002). *The Origins of Status Hierarchies: A Formal Theory and Empirical Test*. American Journal of Sociology, 107(5). DOI: 10.1086/341744.
2. Magee, J. C., & Galinsky, A. D. (2008). *Social Hierarchy: The Self-Reinforcing Nature of Power and Status*. Academy of Management Annals, 2(1), 351–398. DOI: 10.5465/19416520802211628.
3. Bendersky, C., & Pai, J. (2018). *Status Dynamics*. Annual Review of Organizational Psychology and Organizational Behavior, 5, 183–199. DOI: 10.1146/annurev-orgpsych-032117-104602.
4. Smith, J. A., & Faris, R. (2015). *Movement without mobility: Adolescent status hierarchies and the contextual limits of cumulative advantage*. Social Networks, 40, 139–153. DOI: 10.1016/j.socnet.2014.10.004.
5. Overton, J. (2021). *When Does Status Transfer between People? A Crowdsourced Experiment on the Scope of Status by Association*. Social Psychology Quarterly, 84(4), 309–330. DOI: 10.1177/01902725211042313.
6. Henrich, J., & Gil-White, F. J. (2001). *The evolution of prestige: freely conferred deference as a mechanism for enhancing the benefits of cultural transmission*. Evolution and Human Behavior, 22(3), 165–196. DOI: 10.1016/S1090-5138(00)00071-4.
7. Jiménez, Á. V., & Mesoudi, A. (2019). *Prestige-biased social learning: current evidence and outstanding questions*. Palgrave Communications, 5, 20. DOI: 10.1057/s41599-019-0228-7.
8. Berl, R. E. W., Samarasinghe, A., Roberts, S. G., Jordan, F. M., & Gavin, M. C. (2021). *Prestige and content biases together shape the cultural transmission of narratives*. Evolutionary Human Sciences, 3, e42. DOI: 10.1017/ehs.2021.37.
9. Moore, R. A. (1970). *Adoption and Samurai Mobility in Tokugawa Japan*. Journal of Asian Studies, 29(3), 617–632. DOI: 10.2307/2943247.
10. Kumanomido, H., & Takayasu, Y. (2026). *Elite persistence in family: The role of adoption in prewar Japan*. Economic History Review. DOI: 10.1111/ehr.70132.
11. Sauder, M., Lynn, F., & Podolny, J. M. (2012). *Status: Insights from Organizational Sociology*. Annual Review of Sociology, 38, 267–283. DOI: 10.1146/annurev-soc-071811-145503.
12. Ridgeway, C. L. (2026). *Status*. Oxford Research Encyclopedia of Sociology. DOI: 10.1093/9780197852729.003.0132.

---

## 版本註記

v0.4 的主要進展：

$$
\boxed{
\text{status feedback}
\text{ is not the frontier}
}
$$

新的候選前沿是：

$$
\boxed{
\text{status persistence across carrier substitution}.
}
$$

尤其是：

$$
\boxed{
P
\rightarrow
H/O/N/R
\rightarrow
P'
}
$$

這使日本悖論原有的：

$$
\text{House Continuity}
$$

第一次能直接與：

$$
\text{Heroization},
\text{Status Persistence},
\text{Enemy Reintegration}
$$

放在同一個可檢驗架構中。
