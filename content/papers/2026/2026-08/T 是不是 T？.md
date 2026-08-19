# T 是不是 T？
## 多重身份關係下的判定、欠定義與身份查詢語義學

**英文題名：** *Is T Really T? Judgment, Underdetermination, and Query Semantics under Multiple Identity Relations*  
**系列：**《T 的九問：符號身份、生成、命名與持續》Paper 02  
**版本：** v0.1 理論草稿  
**日期：** 2026-08-12  
**作者：** Neo.K、Aletheia（AI 協作）  
**機構：** EveMissLab／一言諾科技有限公司

---

## 摘要

本文延續 Paper 01 的多重同一性符號學（Multi-Identity Semiotics, MIS）與符號身份動力學（Symbolic Identity Dynamics, SID），將問題從「T 可以在哪些身份維度上相同或不同」推進至更具操作性的問題：

> **當我們問「T 是不是 T？」時，一個身份判定系統究竟在判定什麼？**

本文主張，未指定身份判準的 `T_i =? T_j` 通常不是完整的二元問題。身份查詢至少需要指定比較對象、身份判準、判定主體、語境／namespace、時間位置、證據集合與任務。定義身份查詢：

$$
Q_I=(T_i,T_j,\mathcal A,A,c,t,E,\mathcal T),
$$

其中 $\mathcal A$ 是被啟用的身份關係集合。

本文提出四種全域判定狀態：

$$
\boxed{
J(Q_I)\in
\{
\mathrm{Same},
\mathrm{Different},
\mathrm{Both},
\mathrm{Underdetermined}
\}
}
$$

但這四個輸出不是四個真值。`Both` 表示不同身份關係得到不同方向的合法判定，例如「字形相同但 token 不同」；`Underdetermined` 則表示身份問題因判準、證據、語境、時間或 namespace 不足而尚未形成唯一可執行答案。

本文建立局部身份判定器、身份證據向量、判準集合聚合、觀察者限制、身份查詢完整性、判準精化與身份判定穩定性，並證明：

$$
\boxed{
\mathrm{Both}
\not\Rightarrow
\text{Logical Contradiction}
}
$$

因為：

$$
T_i\equiv_{\alpha}T_j
$$

與：

$$
T_i\not\equiv_{\beta}T_j
$$

在 $\alpha\neq\beta$ 時並不是同一命題與其否定。

---

## 關鍵詞

多重同一性、身份判定、相對同一性、欠定義、身份查詢、Same/Different/Both/Underdetermined、符號身份、判準集合、身份證據、身份語義學

---

# 0. 研究邊界

本文不主張：

1. 傳統二值邏輯中的等號必須改成四值等號；
2. 真正的數值同一律 $x=x$ 是不確定的；
3. `Both` 表示同一命題 $P$ 與 $\neg P$ 在相同條件下同時成立；
4. `Underdetermined` 必然表示世界本體本身模糊；
5. 觀察者可以任意決定身份；
6. 身份只是一種主觀語言遊戲；
7. 相對同一性理論已經等同本文的完整框架；
8. 本文四種輸出需要採用某個既有四值邏輯才能成立。

本文研究的是：

> **當「相同」這個自然語言詞彙同時壓縮多種身份關係時，系統如何先展開問題，再給出可追溯的判定。**

---

# 1. 從 T = T 到 T =? T

Paper 01 的核心形式是：

$$
T_i\equiv_{\alpha,A,c,t}T_j.
$$

本篇進一步問：

$$
\boxed{
T_i\stackrel{?}{\equiv}_{\alpha,A,c,t}T_j
}
$$

如何被判定？

若 $\alpha=G$ 表示 glyph identity，且：

$$
G(T_i)=G(T_j),
$$

則：

$$
J_G(T_i,T_j)=\mathrm{Same}.
$$

但若問題只寫：

> T 是不是 T？

我們不知道要比較 glyph、token、type、state、referent、name、operator、history、namespace 或 temporal continuity。

因此：

$$
\boxed{
T_i\stackrel{?}{=}T_j
}
$$

在多身份框架中常只是未展開查詢。

---

# 2. 相對同一性與本文的差異

哲學中的 relative identity 討論過：

> 兩個對象可以是 same F，但不是 same G。

這與：

$$
T_i\equiv_\alpha T_j
\land
T_i\not\equiv_\beta T_j
$$

具有結構親緣。

但本文的 $\alpha,\beta$ 不限於 sortal predicate，還可表示顯示、byte state、所指、provenance、操作、命名鏈、跨時間連續與制度身份。

所以本文真正研究的是：

$$
\boxed{
\text{identity query over a heterogeneous family of identity relations}.
}
$$

---

# 3. 身份查詢的完整形式

定義：

$$
\boxed{
Q_I=(T_i,T_j,\mathcal A,A,c,t,E,\mathcal T)
}
$$

其中：

- $T_i,T_j$：比較對象；
- $\mathcal A$：身份判準集合；
- $A$：判定主體；
- $c$：語境、namespace 與制度；
- $t$：時間或時間區間；
- $E$：證據集合；
- $\mathcal T$：任務。

若 $\mathcal A=\{G\}$，問題是「是否同形」；若 $\mathcal A=\{R\}$，問題是「是否同所指」；若 $\mathcal A=\{G,X,R,H\}$，則已是複合身份查詢。

---

# 4. 身份查詢完整性

定義：

$$
\operatorname{Complete}(Q_I)
=
C_O\land C_\alpha\land C_C\land C_E,
$$

其中：

- $C_O$：比較對象已解析；
- $C_\alpha$：身份判準已指定；
- $C_C$：語境／namespace 已解析；
- $C_E$：證據最低要求已滿足。

因此：

$$
\boxed{
\neg\operatorname{Complete}(Q_I)
\Rightarrow
J(Q_I)=\mathrm{Underdetermined}
}
$$

是本文的第一條治理原則。

---

# 5. 局部身份判定器

對每個身份關係 $\alpha$ 定義：

$$
J_\alpha(T_i,T_j\mid A,c,t,E).
$$

局部判定至少可採：

$$
\boxed{
J_\alpha\in
\{
\mathrm{Same},
\mathrm{Different},
\mathrm{Unknown},
\mathrm{EvidenceConflict}
\}.
}
$$

例如：

$$
J_G(T_1,T_2)=\mathrm{Same},
$$

而：

$$
J_{\mathrm{token}}(T_1,T_2)=\mathrm{Different}.
$$

若 provenance 缺失：

$$
J_H(T_1,T_2)=\mathrm{Unknown}.
$$

---

# 6. 身份證據向量

定義：

$$
\mathbf E_\alpha=
(E_\alpha^+,E_\alpha^-,E_\alpha^?),
$$

分別表示：

- 支持同一的證據；
- 支持不同的證據；
- 缺失或待查證證據。

因此：

$$
J_\alpha
=
F_\alpha(
E_\alpha^+,
E_\alpha^-,
q(E),
\theta_\alpha
).
$$

身份結論因此具有 provenance，而不只是裸露的 yes/no。

---

# 7. 四種全域輸出

局部判定向量：

$$
\mathbf J=
(J_{\alpha_1},J_{\alpha_2},\ldots,J_{\alpha_n}).
$$

## Same

若所有決定性結果都支持同一：

$$
J(Q_I)=\mathrm{Same}.
$$

## Different

若所有決定性結果都支持不同：

$$
J(Q_I)=\mathrm{Different}.
$$

## Both

若存在：

$$
\exists\alpha,\beta\in\mathcal A
$$

使：

$$
J_\alpha=\mathrm{Same},
\qquad
J_\beta=\mathrm{Different},
$$

則：

$$
\boxed{
J(Q_I)=\mathrm{Both}.
}
$$

## Underdetermined

若判準、對象、namespace、時間、必要證據或任務不足：

$$
\boxed{
J(Q_I)=\mathrm{Underdetermined}.
}
$$

---

# 8. Both 不是矛盾

若：

$$
T_i\equiv_G T_j
$$

且：

$$
T_i\not\equiv_X T_j,
$$

則它們分別是：

$$
P_G(T_i,T_j)
$$

與：

$$
\neg P_X(T_i,T_j).
$$

因此：

$$
P_G\land\neg P_X
$$

不是：

$$
P\land\neg P.
$$

所以：

$$
\boxed{
\mathrm{Both}_{\alpha,\beta}
\not\Rightarrow
\mathrm{Contradiction},
\qquad
\alpha\neq\beta.
}
$$

---

# 9. Relation-Both 與 Evidence-Conflict

必須區分：

## Relation-Both

$$
J_\alpha=\mathrm{Same},
\qquad
J_\beta=\mathrm{Different}.
$$

這是正常的跨身份關係分岔。

## Evidence-Conflict

同一個 $\alpha$ 下：

$$
E_\alpha^+\neq\varnothing,
\qquad
E_\alpha^-\neq\varnothing,
$$

而兩邊證據都超過最低可信閾值。

因此：

$$
\boxed{
\mathrm{Both}_{relation}
\neq
\mathrm{Conflict}_{evidence}.
}
$$

---

# 10. 四種判定狀態不是四值真值邏輯

多值邏輯研究超過兩個 truth values 的形式系統；paraconsistent logic 則研究某些矛盾存在時如何避免爆炸。

本文的：

$$
\{
\mathrm{Same},
\mathrm{Different},
\mathrm{Both},
\mathrm{Underdetermined}
\}
$$

首先是：

$$
\boxed{
\text{Query Resolution Status}
}
$$

而不是 truth-value algebra。

`Both` 可以由兩個普通二值 predicate 產生：

$$
P_\alpha=1,
\qquad
P_\beta=0.
$$

`Underdetermined` 甚至可能只是 $\alpha$ 根本沒有被指定。

---

# 11. 六種欠定義

## 11.1 Criterion Underdetermination
沒有指定要比較哪種身份。

## 11.2 Evidence Underdetermination
知道比較 provenance，但證據不完整。

## 11.3 Namespace Underdetermination
同一符號在不同 namespace 中有不同 identity。

## 11.4 Temporal Underdetermination
沒有指定比較的時間點或區間。

## 11.5 Granularity Underdetermination
「同一本書」可能指同作品、同版本、同檔案、同實體或同掃描件。

## 11.6 Task Underdetermination
對備份系統相同 content hash 可能足夠；對法律原件卻可能還需要 provenance。

所以：

$$
\boxed{
\text{Same enough for task A}
\neq
\text{Same enough for task B}.
}
$$

---

# 12. 觀察者不是任意主宰

主體 $A$ 必須受到：

$$
\boxed{
\mathcal C_A=
(
\text{Evidence Access},
\text{Admissible Rules},
\text{Task},
\text{Authority},
\text{Auditability}
)
}
$$

限制。

因此 $A$ 是：

$$
\boxed{
\text{bounded identity judge}.
}
$$

而不是可以任意指定身份的造物主。

---

# 13. 主體分歧與身份判定差分

兩個主體：

$$
A,B
$$

可能得到：

$$
J_A(Q_I)\neq J_B(Q_I).
$$

原因可能是：

- 證據集合不同；
- 判準不同；
- namespace 不同；
- 閾值不同。

定義：

$$
\boxed{
\Delta_{AB}^{I}
=
\operatorname{Diff}(Q_A,Q_B).
}
$$

成熟系統應回報分歧來源，而不是只說「兩個人看法不同」。

---

# 14. 判準精化

若：

$$
\mathcal A_1=\{G\}
$$

得到：

$$
J(Q_1)=\mathrm{Same},
$$

後來加入：

$$
\mathcal A_2=\{G,X\},
$$

且：

$$
J_G=\mathrm{Same},
\qquad
J_X=\mathrm{Different},
$$

則：

$$
J(Q_2)=\mathrm{Both}.
$$

這不是對象改變，而是：

$$
\boxed{
\text{Criterion Refinement}
\rightarrow
\text{Judgment Refinement}.
}
$$

---

# 15. 命題一：未索引身份查詢的不唯一性

若存在：

$$
\alpha,\beta
$$

使：

$$
T_i\equiv_\alpha T_j
$$

且：

$$
T_i\not\equiv_\beta T_j,
$$

則未指定身份關係的：

$$
T_i\stackrel{?}{=}T_j
$$

不能由這些關係唯一決定。

因為選 $\{\alpha\}$ 得到 Same，選 $\{\beta\}$ 得到 Different。

$$
\boxed{\square}
$$

---

# 16. 命題二：Relation-Both 的非矛盾性

若 $\alpha\neq\beta$，則：

$$
T_i\equiv_\alpha T_j
$$

與：

$$
T_i\not\equiv_\beta T_j
$$

是不同關係命題。

因此：

$$
P_\alpha\land\neg P_\beta
$$

不等於：

$$
P_\alpha\land\neg P_\alpha.
$$

$$
\boxed{\square}
$$

---

# 17. 命題三：判準精化可改變答案而不改變對象

令：

$$
\mathcal A_1=\{G\},
$$

$$
\mathcal A_2=\{G,\mathrm{token}\}.
$$

若兩個 token 字形相同：

$$
J_G=\mathrm{Same},
$$

但 token 不同：

$$
J_{\mathrm{token}}=\mathrm{Different},
$$

則：

$$
J(Q_{\mathcal A_1})=\mathrm{Same},
$$

而：

$$
J(Q_{\mathcal A_2})=\mathrm{Both}.
$$

所以：

$$
\boxed{
\Delta J\not\Rightarrow\Delta T.
}
$$

---

# 18. TTTTT 的第一個身份矩陣

考慮：

$$
T_1T_2T_3T_4T_5.
$$

例如：

| 關係 | $T_1,T_2$ | $T_1,T_3$ |
|---|---|---|
| Glyph | Same | Same |
| Type | Same | Same |
| Token | Different | Different |
| State | Same | Different |
| Referent | Same | Unknown |
| History | Different | Different |

因此兩組全域輸出都可能是 `Both`，但其內部結構不同。

定義：

$$
\boxed{
\mathbf J_I(T_i,T_j)
=
(
J_G,J_\tau,J_X,J_R,J_N,J_O,J_H,J_C,J_T
)
}
$$

為 Identity Judgment Vector。

全域標籤只是：

$$
\boxed{
J(Q_I)
=
\operatorname{Compress}_{\mathcal T}(\mathbf J_I).
}
$$

---

# 19. 身份答案本身也是投影

Paper 01 有：

$$
x\xrightarrow{\Pi}T,
$$

即狀態投影為可見符號。

Paper 02 則有：

$$
\mathbf J_I
\xrightarrow{\Pi_J}
\mathrm{Same/Both/\cdots}.
$$

所以：

$$
\boxed{
\text{符號可以是投影，身份答案也可以是投影。}
}
$$

「它們一樣」可能只是對高維 identity profile 的任務相對低維摘要。

---

# 20. Identity Decision Package

只保存：

```text
same = true
```

或：

```text
same = false
```

會丟失判定理由。

因此定義：

$$
\boxed{
IDP=(Q_I,\mathbf J_I,J,E,P,V)
}
$$

其中：

- $Q_I$：身份查詢；
- $\mathbf J_I$：局部判定向量；
- $J$：全域摘要；
- $E$：證據；
- $P$：provenance；
- $V$：判定器／規則版本。

這使身份判定可重播、審計、修正與跨時間重新計算。

---

# 21. T 是不是 T 的時間版本

加入：

$$
t_0,t_1.
$$

若：

$$
J_X=\mathrm{Different},
$$

但：

$$
J_H=\mathrm{Same},
$$

則：

$$
J=\mathrm{Both}.
$$

這就是：

> 它變了，但還是它。

---

# 22. T 是不是 T 的命名版本

若：

$$
N(T_i)=N(T_j)=T,
$$

但：

$$
R(T_i)\neq R(T_j),
$$

則：

$$
J_N=\mathrm{Same},
$$

而：

$$
J_R=\mathrm{Different}.
$$

所以：

$$
\boxed{
\text{Same Name}
\not\Rightarrow
\text{Same Referent}.
}
$$

---

# 23. 單符號宇宙下的身份判定

若所有 glyph 都是：

$$
T,
$$

則：

$$
J_G
$$

幾乎永遠輸出 Same。

因此 glyph criterion 的 discriminative power：

$$
D_G\rightarrow0.
$$

單符號宇宙不是讓身份問題消失，而是迫使系統使用更高階 identity criteria。

---

# 24. 身份判準的信息價值

定義：

$$
IG(\alpha\mid Q,\mathcal T)
$$

表示身份判準 $\alpha$ 對當前查詢的資訊增益。

如果所有 T 都同形：

$$
IG(G)\approx0,
$$

但：

$$
IG(X)
$$

或：

$$
IG(H)
$$

可能很高。

所以身份系統可以主動選擇：

$$
\boxed{
\alpha^*
=
\arg\max_\alpha
IG(\alpha\mid Q,\mathcal T).
}
$$

這稱為 Active Identity Resolution。

---

# 25. 最小充分身份查詢

若存在最小判準集合：

$$
\mathcal A^*
$$

使其足以完成任務，而任何真子集都不足，則：

$$
\boxed{
\mathcal A^*
=
\arg\min_{\mathcal A}|\mathcal A|
\quad
\text{s.t.}
\quad
\operatorname{Sufficient}(\mathcal A,\mathcal T).
}
$$

這避免：

- 比較太少造成 identity collapse；
- 比較太多造成 identity over-fragmentation。

---

# 26. AI 身份系統的應用

假設一個 Agent：

- 模型從 $M_1$ 換成 $M_2$ ；
- 記憶保留；
- 名稱保留；
- 長期目標保留；
- 身份 ID 保留；
- 行為風格部分改變。

若只採：

$$
\alpha=\mathrm{model},
$$

答案是 Different。

若採：

$$
\alpha=H
$$

與：

$$
\alpha=N,
$$

可能是 Same。

因此：

$$
J=\mathrm{Both}.
$$

這不是逃避回答，而是在暴露原問題同時包含多個身份問題。

---

# 27. 資料與程式身份

即使：

$$
Hash(f_1)=Hash(f_2),
$$

支持 content identity，也不保證 provenance、owner、creation history 相同。

所以：

$$
\boxed{
\text{Same Bytes}
\not\Rightarrow
\text{Same Artifact Identity}.
}
$$

---

# 28. 認識論欠定義與本體欠定義

`Underdetermined` 還需標記來源。

可能只是：

$$
\mathrm{MissingEvidence},
$$

也可能是：

$$
\mathrm{CriterionNotSpecified},
$$

或：

$$
\mathrm{NamespaceConflict}.
$$

本文不在此強迫決定「世界本身是否真的具有模糊身份」，而要求系統至少先說清楚欠定義來自哪裡。

---

# 29. Identity Epistemic Discipline

如果證據與判準不足：

$$
\boxed{
\text{Do not collapse Underdetermined into Same or Different.}
}
$$

否則會產生：

- False Merge：不同身份被錯誤合併；
- False Split：持續身份被錯誤分裂。

---

# 30. Paper 02 的核心算子

整篇可以壓成：

$$
\boxed{
\mathfrak J_I:
(
T_i,T_j,\mathcal T,A,c,t,E
)
\longrightarrow
(
\mathcal A,
\mathbf J_I,
J,
\mathcal G
)
}
$$

其中：

- $\mathcal A$：選出的身份判準；
- $\mathbf J_I$：多維局部判定；
- $J$：全域摘要；
- $\mathcal G$：身份 grounding / evidence certificate。

因此「T 是不是 T？」第一次成為一個可執行的型別化查詢。

---

# 31. 與既有研究的邊界

外部哲學研究已長期討論 relative identity、vague/indeterminate identity，以及多值與 paraconsistent logic。

MIS/SID 的新增工作不是宣稱這些問題從未存在，而是：

1. 將多種 identity relations 同時顯式化；
2. 把 observer、namespace、time、evidence、task 放入 query；
3. 將 `Both` 定義為跨 relation divergence；
4. 將 `Underdetermined` 拆成不同來源；
5. 保存 Identity Judgment Vector；
6. 允許身份判準依任務主動選擇。

---

# 32. 核心命題總結

## A. 身份查詢索引必要性

$$
\operatorname{Same}(x,y)
$$

應允許展開為：

$$
\operatorname{Same}(x,y\mid\mathcal A,A,c,t,E,\mathcal T).
$$

## B. Both 非矛盾性

$$
\exists\alpha\neq\beta:
x\equiv_\alpha y
\land
x\not\equiv_\beta y
$$

不構成：

$$
P\land\neg P.
$$

## C. 欠定義保留原則

$$
\boxed{
\neg\operatorname{Complete}(Q_I)
\Rightarrow
J(Q_I)=\mathrm{Underdetermined}.
}
$$

## D. 答案變化不等於對象變化

$$
\boxed{
\Delta J\not\Rightarrow\Delta T.
}
$$

## E. 全域標籤是身份向量的投影

$$
\boxed{
J=\Pi_{\mathcal T}(\mathbf J_I).
}
$$

---

# 33. 結論

最開始：

$$
T\stackrel{?}{=}T
$$

看起來是一個最簡單的問題。

真正展開後，它變成：

$$
\boxed{
Q_I=
(
T_i,T_j,\mathcal A,A,c,t,E,\mathcal T
).
}
$$

所以「T 是不是 T？」可能回答 Same、Different、Both，甚至最正確的是 Underdetermined。

問題不在於邏輯突然失效。

而在於：

$$
\boxed{
\text{我們以前把很多不同的「同一」壓成了一個等號。}
}
$$

因此 Paper 02 的最終命題是：

$$
\boxed{
\text{Before answering whether T is T, resolve what “same” is asking for.}
}
$$

下一篇 Paper 03〈T 為什麼是 T？〉將研究 Identity Grounding、身份不變量、provenance、證據與 Identity Certificate。
