# 從重建到閉合：自主數學研究代理循環在穩定 Kneser 圖上的多輪實驗

## ——RIITG、RAB、KCPE 與自我修正證明工程的一次完整研究紀錄

**作者：Neo.K（理論構想與研究方向）／Aletheia（協作推演、計算與形式整理）**  
**版本：v1.0 初版研究紀錄稿**  
**日期：2026-07-11**  
**系列定位：三篇論文之一——第一篇：實際研究推進紀錄**

---

## 重要聲明

本文記錄的是一場多輪數學研究實驗。其主要目的不是宣稱某一既有定理的世界首證，而是檢驗下列方法能否被持續執行：

$$
\mathrm{RIITG}
+
\mathrm{RAB}
+
\mathrm{KCPE}
+
\mathrm{AMRAL}.
$$

其中：

- RIITG：結果誘導的中介定理生成法；
- RAB：逆向公理回填法；
- KCPE：知識條件化的證明空間類窮舉；
- AMRAL：自主數學研究代理循環。

本文保留成功、錯誤、反例、方法族淘汰、重新定義、有限計算、文獻吸收與最終閉合的完整順序。

本文不主張：

1. 所有推演均完全不受模型先驗知識影響；
2. 所有中間結論皆為首次發現；
3. 最後得到的色數定理具有世界首證地位；
4. 本文已證明上述 Agent 方法對所有數學問題均有效；
5. 計算輔助部分可以在沒有程式與輸出紀錄時被視為純手證。

本文主張的是：

$$
\boxed{
\text{一個研究問題確實被反覆轉化、剪枝、驗證、否證、回填與重新閉合。}
}
$$

而且整個路徑留下了：

- 可重跑程式；
- 明確證明義務；
- 被否定的方法族；
- 已知文獻對照；
- 有限核心證書；
- 可由後續 Agent 直接接續的研究狀態。

---

## 摘要

本文報告一場以 Kneser–Lovász 著色下界及其穩定版本為目標的多輪自主數學研究實驗。實驗起點是一套由結果反向生成中介命題、再由基礎正向回填的證明工程方法。與一次性證明搜索不同，本研究將數學研究表示為狀態序列：

$$
\mathcal S_0
\rightarrow
\mathcal S_1
\rightarrow
\cdots
\rightarrow
\mathcal S_T.
$$

每個狀態包含目標、候選橋樑、知識庫、計算結果、失敗紀錄、證明依賴與尚未完成的回填義務。

第一階段以已知 Kneser–Lovász 定理作為受污染條件下的準盲目標。系統生成直接計數、譜方法、多項式方法、壓縮、穩定核心、鄰域複形、反足障礙與 Tucker 標記等候補路線。基本 EKR 容量與一階譜界被快速降權，因其主要停留在約 $n/k$ 的尺度；Tucker 路線則完成一條已知組合證明的重建。小參數計算同時重新辨認出 Schrijver 穩定核心。

第二階段從穩定核心出發，重新回填一個低次多項式的穩定正號選擇引理。透過循環正號區塊數、同號相鄰邊數與介值定理，得到「區塊數—根數」橋樑。該橋樑在 $s=2$ 成功，但直接推廣到 $s>2$ 時失敗。有限窮舉進一步顯示，單一二元 carrier 加一階根計數在若干 $s=3,4$ 小參數中不足；多 carrier 雖能覆蓋低次符號型，卻破壞反足排他性。單值 selector 與局部一致 atlas 隨後分別被精確不可行性與理論塌縮論證否定。

第三階段轉向 $k=2$ 的純組合結構。由兩兩相交的 2-集合族必為 star 或 triangle，著色問題被改寫成 stars/triangles cover。研究過程先產生一個錯誤的「殘餘邊必位於內部三角形」命題，之後主動修正為 triangle/singleton block cover。大參數由解析邊數界閉合，小參數則由 exact verifier 完成；事後文獻審計顯示 $k=2$ 的更廣結果已知，故該階段被標記為重建而非新定理。

第四階段推進至 $s=3,k=3$ 。利用 maximal intersecting 3-set families 的完整分類，色類被壓縮為 star、pair-kernel 與有限例外模板。初始粗界將假想反例壓成 23 點核心；進一步使用循環單調嵌入與 stable-specific 容量，將 non-star 色類最大容量修正為：

$$
M(r)=3r-28.
$$

此修正使解析 star-forcing 門檻下降至 $r\ge15$ 。對 $10\le r\le14$ ，本文附帶精確有理數 LP 對偶證書，證明任何 $(r-7)$ -著色必含 star 色類。反覆刪除 star 中心與對應顏色，將任意假想反例降至 $r=9$ ，但 $KG(9,3)_{3\text{-stab}}\cong K_3$ 不可二著色，矛盾。由此得到一條計算輔助的完整閉合路線：

$$
\chi\!\left(KG(r,3)_{3\text{-stab}}\right)=r-6.
$$

公開的 2026 年研討會與學位論文資訊顯示，同時期已有研究團隊處理 $s=3$ 的剩餘情形，故本文不宣稱定理首證。本文的主要成果是展示一條由錯誤保存、方法族否證、模板壓縮、有限核心、精確證書與星剝離所構成的可審計研究路徑。

本文的核心結論不是「Agent 一次猜中答案」，而是：

$$
\boxed{
\text{持續研究可以被實作為一個會保存失敗、會推翻自己、並能逐輪縮小 GAP 的狀態動力系統。}
}
$$

**關鍵詞：** 自主數學研究 Agent、Kneser 圖、穩定 Kneser 圖、結果誘導、中介定理、逆向公理回填、知識條件化類窮舉、計算輔助證明、有限核心、星剝離、研究狀態

---

# 1. 研究背景與方法定位

## 1.1 從單次證明到研究狀態演化

傳統自動定理證明可粗略表示為：

$$
(\mathcal T,P)
\longrightarrow
\operatorname{Proof}(P),
$$

其中 $\mathcal T$ 是固定理論， $P$ 是目標。

本研究採用不同模型：

$$
\mathcal S_t
=
(
P_t,
\mathcal K_t,
\mathcal M_t,
\Omega_t,
\mathcal F_t,
\mathcal C_t,
\mathcal D_t
),
$$

其中：

- $P_t$ ：當前目標；
- $\mathcal K_t$ ：內部、外部與形式知識；
- $\mathcal M_t$ ：候選中介命題；
- $\Omega_t$ ：候補路線空間；
- $\mathcal F_t$ ：失敗與反例；
- $\mathcal C_t$ ：計算結果；
- $\mathcal D_t$ ：證明依賴圖。

每一輪不必完成證明，只需使研究狀態發生有資訊增益的轉移：

$$
\mathcal S_{t+1}
=
\mathcal U(
\mathcal S_t,
\mathcal F_t,
\mathcal C_t,
\Delta\mathcal K_t
).
$$

---

## 1.2 四個核心組件

### RIITG

由目標命題反向生成足以導向目標的中介節點：

$$
P
\rightsquigarrow
\mathcal M.
$$

這不是合法推理規則，而是搜索算子。

### RAB

將暫態橋樑全部降格為證明義務：

$$
\mathcal T
\Rightarrow
\mathcal M
\Rightarrow
P.
$$

### KCPE

不窮舉全部數學命題，而是在知識、失敗、語義窗口與預算限制下構造局部搜索域：

$$
\Omega_t
=
\Omega(
P_t,
\mathcal K_t,
\mathcal F_{<t},
W_{\mathrm{sem}},
B_t
).
$$

### AMRAL

將生成、回填、計算、反證、文獻檢索與狀態更新組成持續循環：

$$
\text{Analyze}
\rightarrow
\text{Generate}
\rightarrow
\text{Enumerate}
\rightarrow
\text{Retrieve}
\rightarrow
\text{Backfill}
\rightarrow
\text{Compute}
\rightarrow
\text{Verify}
\rightarrow
\text{Falsify}
\rightarrow
\text{Update}.
$$

---

# 2. 實驗起點：Kneser–Lovász 下界

## 2.1 目標

Kneser 圖 $KG(n,k)$ 的頂點為所有 $k$ 元子集，兩頂點相鄰當且僅當它們不交。

已知色數為：

$$
\chi(KG(n,k))
=
n-2k+2.
$$

本實驗先測試下界：

$$
\chi(KG(n,k))
\ge
n-2k+2.
$$

令：

$$
q=n-2k+1.
$$

反設存在 proper coloring：

$$
c:
\binom{[n]}k
\rightarrow
[q].
$$

研究問題轉化為：

> 低色數假設必然生成什麼不可能結構？

---

## 2.2 初始候補路線

第一輪生成十二類候補：

1. 直接計數；
2. 最小元素逆向；
3. 分數著色／線性規劃；
4. 譜界；
5. 多項式／線性代數；
6. 壓縮與 shifting；
7. 鄰域複形；
8. 反足與等變障礙；
9. Tucker 標記；
10. 穩定核心；
11. 概率與熵；
12. 證明複雜度。

此時並不預設哪條路線正確。

---

# 3. 第一輪剪枝：一階容量不足

每個色類都是 intersecting family。

由最大交集族尺度，只能得到：

$$
\chi(KG(n,k))
\ge
\frac{\binom nk}{\binom{n-1}{k-1}}
=
\frac nk.
$$

基本 Hoffman 譜界也落在同一量級。

例如：

$$
(n,k)=(10,2),
$$

則：

$$
\frac nk=5,
$$

而目標為：

$$
8.
$$

因此得到第一個方法族淘汰資訊：

$$
\boxed{
\text{一階容量與基本譜尺度不足以直接閉合目標。}
}
$$

這不等於所有代數或譜方法不可能，而是證明需要更高階結構。

---

# 4. 第一輪閉合：Tucker 路線重建

## 4.1 符號向量

考慮：

$$
X=
\{-1,0,1\}^n\setminus\{0\}.
$$

定義：

$$
x^+=\{i:x_i=1\},
\qquad
x^-=\{i:x_i=-1\}.
$$

並以支撐包含定義偏序：

$$
x\preceq y
\iff
x^+\subseteq y^+,\ 
x^-\subseteq y^-.
$$

---

## 4.2 標記構造

利用 alternation number 與假想著色 $c$ ，構造：

$$
\lambda:
X
\rightarrow
\{\pm1,\dots,\pm(n-1)\}
$$

滿足：

$$
\lambda(-x)=-\lambda(x).
$$

對小 alternation number，以第一個非零符號定向；對大 alternation number，分別查看 $x^+$ 與 $x^-$ 中可包含的 $k$-集合顏色。

proper coloring 的不交排他性保證，不可能在正負支撐中同時出現同色 $k$-集合。

---

## 4.3 互補可比較對不可能

可證：

$$
x\preceq y
\Rightarrow
\lambda(x)\neq-\lambda(y).
$$

但 octahedral Tucker lemma 在標號數 $m<n$ 時強迫存在：

$$
x\preceq y,
\qquad
\lambda(x)=-\lambda(y).
$$

矛盾。

因此：

$$
\chi(KG(n,k))
\ge
n-2k+2.
$$

這條路線與既有 Tucker 型組合證明高度一致，故標記為：

$$
\mathrm{Reconstruction},
$$

而非新證明。

---

# 5. 計算再發現：Schrijver 穩定核心

## 5.1 小參數刪點

對：

$$
KG(6,2),\ KG(7,2),\ KG(8,2),
$$

反覆刪除在刪後仍保持目標色數的頂點，得到核心大小：

$$
9,\ 14,\ 20.
$$

這些數值符合：

$$
\binom n2-n.
$$

進一步辨認後，核心同構於循環上不取相鄰點的 stable 2-subsets 誘導子圖。

---

## 5.2 文獻吸收

事後檢索確認，這正是 Schrijver 1978 年建立的 vertex-critical stable subgraph。

因此：

$$
\boxed{
\text{計算模式}
\rightarrow
\text{結構猜想}
\rightarrow
\text{文獻辨認}
}
$$

成為本實驗第一次完整展示的知識底空間擴張。

---

# 6. 第二輪：區塊數—根數橋樑

## 6.1 低次多項式選擇問題

令：

$$
d=N-2k.
$$

希望證明：對任意非零實多項式 $p$ ，若：

$$
\deg p\le d,
$$

則存在循環 stable $k$ -subset $S$ ，滿足：

$$
(-1)^ip(i)>0
\qquad
\forall i\in S.
$$

---

## 6.2 正號區塊

令：

$$
a_i=(-1)^ip(i).
$$

假設正號位置不含 stable $k$-subset。

令正號循環區塊數為 $c$ 。

每個正號區塊至少能提供一個互不相鄰正點，所以：

$$
c\le k-1.
$$

二元循環序列中的同號邊數至少：

$$
N-2c
\ge
N-2k+2
=
d+2.
$$

去掉首尾循環邊後，線性相鄰對中至少仍有：

$$
d+1
$$

個同號 $a_i,a_{i+1}$ 。

---

## 6.3 根數矛盾

若：

$$
a_i
$$

與：

$$
a_{i+1}
$$

同號，因為交替因子變號：

$$
(-1)^{i+1}=-(-1)^i,
$$

所以：

$$
p(i)p(i+1)<0.
$$

每一個相鄰區間產生一個不同實根。

故 $p$ 至少有：

$$
d+1
$$

個根，與：

$$
\deg p\le d
$$

矛盾。

整數採樣零點可透過小插值擾動處理，而不改變正號位置。

---

## 6.4 狀態

此結果不是整條 Kneser 定理的新證明，而是一個候選簡化的中介證明：

$$
\text{選擇失敗}
\Rightarrow
\text{區塊少}
\Rightarrow
\text{變號多}
\Rightarrow
\text{根過多}.
$$

---

# 7. 第三輪：一般化失敗與方法族否證

## 7.1 推向 $s$-stable

自然嘗試是將相鄰同號邊計數推到 $s>2$ 。

但所需色數尺度為：

$$
N-s(k-1),
$$

而一階相鄰根計數只能產生遠低於目標的保證。

---

## 7.2 單一 carrier 的有限障礙

考慮固定二元 carrier：

$$
\sigma\in\{\pm1\}^N.
$$

對低次多項式符號型，研究：

$$
P_\sigma(p)
=
\{i:\sigma_ip(i)>0\}.
$$

完整枚舉小參數後發現：

- $s=2$ 時最佳 carrier 可達所需根數；
- $s=3$ 時在測試案例中通常恰差一根；
- $s=4$ 缺口更大。

因此有限參數下可排除：

$$
\boxed{
\text{單固定 binary carrier}
+
\text{一階相鄰 root-count}
}
$$

作為一般閉合機制。

---

## 7.3 多 carrier

將 carrier 擴張為有限族：

$$
\Sigma=
\{\sigma^{(1)},\dots,\sigma^{(m)}\}.
$$

對若干 $s=3$ 小參數，兩至三個 carrier 可以覆蓋所有 degree-$d$ 可實現符號型。

但新的問題是：在 $a$ 與 $-a$ 兩個反足方向使用不同 carrier 時，兩個 witness stable sets 不再自動不交。

新 GAP 因此變成：

$$
G_{\mathrm{anti-compatible}}
=
\text{多 carrier 如何保留反足排他性？}
$$

---

# 8. 第四輪：selector 與 atlas 的失敗

## 8.1 單值 selector

希望為每個符號面 $x$ 選擇一個 stable witness $A(x)$ ，並要求：

$$
x\preceq y
\Rightarrow
A(x)\cap A(-y)=\varnothing.
$$

最小案例可行，但在下一個小參數模型中，即使允許每個符號面自由選擇任意 stable pair，精確整數模型仍不可行。

因此：

$$
\boxed{
\text{單值、序相容、反足不交 selector 太強。}
}
$$

---

## 8.2 局部一致 atlas

另一候補是讓不同 carrier 僅負責局部座標域，且在重疊區符號一致。

但重疊一致性使局部符號可以拼接成全域 carrier；該全域 carrier 的覆蓋能力不弱於局部 atlas 的聯集。

所以：

$$
\boxed{
\text{pairwise-compatible local atlas}
\Rightarrow
\text{single global carrier}.
}
$$

這條路線理論塌縮。

---

## 8.3 拓撲訊號

carrier-witness nerve 在刪除破壞不交性的 bad faces 後，有限計算仍顯示非平凡高維同調。

這提供了後續 deleted-join 或 $\mathbb Z_2$-index 方向的研究訊號，但本實驗未在此閉合。

---

# 9. 第五輪：轉向 $k=2$ 的 stars/triangles cover

## 9.1 色類結構

任何兩兩相交的 2-集合族必為：

1. star 子族；
2. triangle 子族。

因此 $k=2$ 的 stable-Kneser 著色可改寫成 stars/triangles cover。

---

## 9.2 初始錯誤

初始命題聲稱：

> 移除 star centers 後，所有剩餘邊必位於殘餘圖內部三角形中。

此命題錯誤，因為 triangle color 的第三個點可能位於殘餘點集外。

---

## 9.3 修正

正確 block 為：

- internal triangle；
- singleton edge。

令 $\tau_N(R)$ 為覆蓋殘餘邊所需最少 block 數。

目標變成：

$$
\tau_N(R)\ge |R|-3.
$$

---

## 9.4 大核心解析界

殘餘圖為：

$$
H_N[R]
=
K_r-C_N^2[R].
$$

由：

$$
\Delta(C_N^2[R])\le4
$$

可得：

$$
e(H_N[R])
\ge
\binom r2-2r.
$$

每個 block 最多覆蓋三條邊。

當：

$$
r\ge9,
$$

邊數下界即推出：

$$
\tau_N(R)\ge r-3.
$$

---

## 9.5 小核心 exact verifier

對：

$$
4\le r\le8,
$$

利用截斷循環 gap：

$$
\widehat g_i=\min(g_i,3)
$$

將無限配置壓為有限字：

$$
\widehat g\in\{1,2,3\}^r.
$$

exact branch-and-bound verifier 重新執行結果：

```text
checked patterns: {4: 76, 5: 242, 6: 729, 7: 2187, 8: 6561}
counterexamples: []
```

因此 $s=3,k=2$ 路線閉合。

事後文獻審計顯示 $k=2$ 的更廣 stable-Kneser 結果已存在，故本階段屬重建與方法驗證。

---

# 10. 第六輪： $k=3$ 的有限模板壓縮

## 10.1 完整 intersecting 3-set 分類

任何 color class 都是 intersecting 3-family，並可擴張為 maximal intersecting family。

已知完整分類將其分為：

- star；
- 三條 pair-rays 型；
- 中心加三條 rays 與例外 triple 型；
- 兩條 rays 加有限例外型；
- 一條 ray 加有限例外型；
- 八種有限 exceptional families。

所以色類搜索不再是任意子集搜索，而是有限模板搜索。

---

## 10.2 三個尺度

以 transversal number 分層：

$$
\tau=1,\quad \tau=2,\quad \tau=3.
$$

對應容量尺度：

$$
O(r^2),
\quad
O(r),
\quad
O(1).
$$

即：

$$
\boxed{
\text{star}
\rightarrow
\text{pair-kernel}
\rightarrow
\text{finite exception}.
}
$$

---

# 11. 初始 23 點核心與其修正

## 11.1 粗 non-star 容量

先使用：

$$
|\mathcal F|\le3r-8
$$

的粗尺度，結合殘餘 stable triples 下界，得到假想反例可壓至：

$$
r\le24.
$$

等號分析排除 $r=24$ ，得到：

$$
r\le23.
$$

---

## 11.2 重要修正

後續發現，不必枚舉所有 gap words。

把殘餘點集 $R$ 按循環順序重新編號，任何在小循環 $C_r$ 上 3-stable 的 triple，映回原循環後仍 3-stable。

因此：

$$
KG(r,3)_{3\text{-stab}}
\subseteq
G(R).
$$

無限 gap-core 搜索被壓縮為完整小循環序列。

---

# 12. 決戰修正： $3r-27$ 到 $3r-28$

## 12.1 定義

令：

$$
M(r)
=
\max
\left\{
|\mathcal F|:
\mathcal F
\subseteq
V(KG(r,3)_{3\text{-stab}}),
\ \mathcal F\text{ intersecting且非 star}
\right\}.
$$

初始估計為：

$$
M(r)\le3r-27.
$$

獨立枚舉與逐型重算後，修正為：

$$
\boxed{
M(r)=3r-28
}
\qquad
(r\ge15).
$$

---

## 12.2 Pair-ray 容量

固定 3-stable pair $\{a,b\}$ 。

所有使 $\{a,b,x\}$ 仍 3-stable 的 $x$ ，必避開：

$$
B_2(a)\cup B_2(b).
$$

若 pair 距離為 $3$ ，該聯集最小為 $8$ ，所以一條 ray 最多有：

$$
r-8
$$

個 stable triples。

---

## 12.3 Type 2

三條 rays：

$$
\{abx,\ acy,\ bcz\}.
$$

三個 kernel pairs 不可能全部具有最小禁止聯集 $8$ ；最佳情形為：

$$
8,\ 8,\ 10.
$$

kernel triple 被三條 rays 重複計數，故：

$$
|\mathcal F|
\le
3r-(8+8+10)-2
=
3r-28.
$$

有循環 kernel gaps：

$$
3,\ 3,\ r-6
$$

的構造達到等號。

---

## 12.4 Type 3

中心 $a$ 、三 leaves $b,c,d$ ：

$$
\{abx,\ acy,\ adz,\ bcd\}.
$$

若例外 triple $bcd$ 不 stable，則 stable restriction 全部含 $a$ ，成為 star。

非 star 情況迫使 $bcd$ stable。

若三條 rays 均參與，三個 pairwise overlap triples 也 stable，故：

$$
|\mathcal F|
\le
3r-26-3+1
=
3r-28.
$$

其餘模板容量更低。

---

# 13. 解析 star-forcing

完整 3-stable triples 數為：

$$
|V(G_r)|
=
\frac{r(r-7)(r-8)}6.
$$

假設存在：

$$
(r-7)\text{-coloring}
$$

且所有色類皆非 star。

則：

$$
\frac{r(r-7)(r-8)}6
\le
(r-7)(3r-28).
$$

除以 $r-7$ ：

$$
\frac{r(r-8)}6
\le
3r-28.
$$

整理：

$$
(r-12)(r-14)\le0.
$$

所以：

$$
\boxed{
r\ge15
\Rightarrow
\text{每個 }(r-7)\text{-著色必含 star 色類}.
}
$$

---

# 14. 有限核心：精確有理對偶證書

只剩：

$$
10\le r\le14.
$$

為每個 stable triple $A$ 配置非負有理權重 $y_A$ ，使：

$$
\sum_{A\in\mathcal F}y_A\le1
$$

對所有 maximal non-star intersecting family $\mathcal F$ 成立。

若：

$$
\sum_Ay_A>r-7,
$$

則 $r-7$ 個 non-star 色類不可能覆蓋全部頂點。

重新執行 verifier 得：

| $r$ | stable triples | maximal non-star families | 對偶總權重 | 門檻 |
|---:|---:|---:|---:|---:|
| 10 | 10 | 0 | — | 3 |
| 11 | 22 | 11 | $\frac{11}{2}$ | 4 |
| 12 | 40 | 48 | $\frac{11}{2}$ | 5 |
| 13 | 65 | 169 | $\frac{377}{56}$ | 6 |
| 14 | 98 | 448 | $8$ | 7 |

對每一個 maximal non-star family，最大權重皆為：

$$
1.
$$

所以：

$$
\boxed{
10\le r\le14
\Rightarrow
(r-7)\text{-著色必有 star 色類}.
}
$$

---

# 15. 星剝離閉合

假設存在：

$$
(r-7)\text{-著色}.
$$

由前述結果，必有一個共同中心 $x$ 的 star color。

刪除：

- 點 $x$ ；
- 該顏色。

剩餘：

$$
r-1
$$

個循環點，以：

$$
r-8=(r-1)-7
$$

種顏色著色。

按循環順序壓縮後，其中包含：

$$
KG(r-1,3)_{3\text{-stab}}.
$$

所以得到更小反例：

$$
r\rightarrow r-1.
$$

反覆剝離至：

$$
r=9.
$$

但：

$$
KG(9,3)_{3\text{-stab}}
$$

的三個頂點為：

$$
\{1,4,7\},
\quad
\{2,5,8\},
\quad
\{3,6,9\},
$$

三者兩兩不交，形成：

$$
K_3.
$$

它不可二著色。

故不存在 $(r-7)$-著色：

$$
\chi\!\left(KG(r,3)_{3\text{-stab}}\right)
\ge
r-6.
$$

標準最小元素著色給出反向上界，故：

$$
\boxed{
\chi\!\left(KG(r,3)_{3\text{-stab}}\right)
=
r-6
\qquad
(r\ge9).
}
$$

---

# 16. 新穎性與文獻狀態

## 16.1 已知背景

2019 年的研究得到 3-stable Kneser 圖色數下界至多差一色，並指出一般 neighborhood-complex 連通性不足以直接得到完整結論。

2025 年的 intersecting 3-set family 完整分類，提供本文有限模板壓縮所需的主要外部積木。

2026 年公開的研討會與會議摘要顯示，Chen、Parker、Zerbib 等研究者已處理 $s=3$ 的剩餘情形或大參數情形，並使用 stable Hilton–Milner 型結果。

---

## 16.2 本文不能主張的內容

因此本文不能主張：

$$
\text{首次證明 }s=3,k=3\text{ 色數公式}.
$$

目前較合理的標記是：

$$
\boxed{
\mathrm{Independent\ Alternative\ Proof\ Candidate}
}
$$

其特色為：

$$
\text{完整模板分類}
\rightarrow
\text{stable non-star capacity}
\rightarrow
\text{解析 star-forcing}
\rightarrow
\text{有限有理對偶證書}
\rightarrow
\text{star peeling}.
$$

是否與同期未完全公開的證明重合，仍需完整文獻比對。

---

# 17. 研究過程中的主要錯誤與修正

## 17.1 把公理當結論

早期方法論風險：

$$
\text{暫態橋樑}
\not\equiv
\text{已證公理}.
$$

修正：全部降格為 proof obligations。

---

## 17.2 一階尺度錯配

基本 EKR 與譜界只達：

$$
n/k.
$$

修正：尋找結構壓縮與拓撲／標記障礙。

---

## 17.3 $s=2$ 證明天真外推

區塊數—根數依賴相鄰交替。

修正：用有限 carrier 搜索證明整個方法族在 $s>2$ 的不足，而非只說「暫時沒想到」。

---

## 17.4 多 carrier selector 過強

修正：精確不可行性檢查，將失敗定位在反足相容性而非 carrier 數量。

---

## 17.5 局部 atlas 假解

修正：證明重疊一致 atlas 必塌縮成單 carrier。

---

## 17.6 triangle-supported 漏洞

第三點可在殘餘點集外。

修正：改為 internal triangle 或 singleton edge block cover。

---

## 17.7 粗容量常數錯一

$$
3r-27
$$

經獨立枚舉與逐型重算修正為：

$$
3r-28.
$$

該一單位使 star-forcing 門檻由 $16$ 降至 $15$ 。

---

# 18. 方法論評估

## 18.1 本次真正成功的部分

### 候補生成

研究沒有被單一路線綁死。

### 方法族否證

單 carrier、selector 與一致 atlas 均被明確否定。

### 失敗保存

錯誤 generalization 成為後續搜索的剪枝資料。

### 計算與理論互轉

有限模式產生結構猜想，結構猜想又導向解析證明。

### 文獻吸收

一旦發現既有分類或更廣定理，即停止重做並更新知識庫。

### 精確證書

最後的小核心不只依賴「求解器說 infeasible」，而轉成可檢查的有理對偶權重。

---

## 18.2 尚未證明的部分

本次成功不能推出：

$$
\forall P,\ 
\mathrm{AMRAL}(P)\text{ 會收斂}.
$$

仍未證明：

- 候補空間一般會縮小；
- 長期循環不會震盪；
- 語義寬度可以可靠估計；
- 計算成本在更大問題上可控；
- 模型先驗知識污染可以完全分離；
- 同一方法在分析、代數或數論問題上有相同效益。

---

# 19. 證明工程可觀測性

本實驗的重要輸出不只是一個 theorem statement，而是：

$$
O_{\mathrm{PE}}
=
\text{Proof-Engineering Observability}.
$$

其內容包括：

1. 哪些路線被生成；
2. 為什麼被降權；
3. 哪些反例否定了整個方法族；
4. 哪些常數被修正；
5. 哪些計算可以重跑；
6. 哪些文獻使新穎性主張下降；
7. 哪些 GAP 尚未完成。

因此，即使最後定理已被他人證明，研究路徑仍保有方法學價值。

---

# 20. 結論

本次多輪實驗從一個已知 Kneser–Lovász 目標出發，先重建標準證明，再經過穩定核心、多項式橋樑、錯誤一般化、多 carrier、selector 否證、拓撲瓶頸、stars/triangles cover、模板分類、有限核心與星剝離，最終形成一條可審計的計算輔助閉合路線。

整個過程可以概括為：

$$
\text{已知目標}
$$

$$
\Downarrow
$$

$$
\text{多路候補}
$$

$$
\Downarrow
$$

$$
\text{方法族剪枝}
$$

$$
\Downarrow
$$

$$
\text{計算模式}
$$

$$
\Downarrow
$$

$$
\text{錯誤與反例}
$$

$$
\Downarrow
$$

$$
\text{新中介命題}
$$

$$
\Downarrow
$$

$$
\text{有限核心}
$$

$$
\Downarrow
$$

$$
\text{精確證書}
$$

$$
\Downarrow
$$

$$
\text{閉合與新穎性審計}.
$$

所以本實驗最值得保留的結論不是：

> AI 在一次回答中解出一道題。

而是：

$$
\boxed{
\text{Agent 可以透過持續保存研究狀態，逐輪把模糊困難壓成可判定 GAP。}
}
$$

更重要的是：

$$
\boxed{
\text{Agent 必須有能力推翻自己的上一輪，否則它不是研究 Agent。}
}
$$

---

# 附錄 A：研究狀態時間線

| 狀態 | 主要成果 | 狀態標記 |
|---|---|---|
| $\mathcal S_0$ | Kneser 下界與 12 類候補 | Generated |
| $\mathcal S_1$ | Tucker 路線閉合、Schrijver 核心辨認 | Reconstruction |
| $\mathcal S_2$ | 區塊數—根數橋樑 | Structurally useful |
| $\mathcal S_3$ | 單 carrier 一般化失敗、多 carrier 覆蓋 | Mixed |
| $\mathcal S_4$ | selector 不可行、atlas 塌縮 | Refuted family |
| $\mathcal S_5$ | $k=2$ block-cover 修正與 finite verifier | Closed reconstruction |
| $\mathcal S_6$ | $k=3$ 14 型模板壓縮 | Knowledge expansion |
| $\mathcal S_7$ | 23-core 與 gap-monotone 壓縮 | Provisional reduction |
| $\mathcal S_8$ | $M(r)=3r-28$ 、15-threshold | Analytic closure |
| $\mathcal S_9$ | $10\le r\le14$ 有理對偶證書 | Exact finite closure |
| $\mathcal S_{10}$ | star peeling 與新穎性審計 | Closed / novelty limited |

---

# 附錄 B：可重跑工件

## B.1 $s=3,k=2$ cover verifier

檔名：

```text
verify_s3_k2_cover_lemma.py
```

SHA-256：

```text
9fef4396a2af3cd6369469d35604580cc76aa6fd4a743cd7fe56a3aa21970a97
```

## B.2 $s=3,k=3$ finite-core verifier

檔名：

```text
verify_3stable_k3_finite_core.py
```

SHA-256：

```text
de183dd84037c0f146b5be677e693c2cea011ccb15ce57c48d6dc702f94f8db1
```

---

# 附錄 C：結果狀態標記

- **K**：既有已知結果；
- **R**：重建；
- **P**：候選命題；
- **F**：已完成回填；
- **X**：被反例或理論否定；
- **C**：有限計算支持；
- **E**：與目標等價或同等困難風險；
- **N?**：可能具有新穎性但未完成文獻審計；
- **A**：可審計工件存在。

---

# 附錄 D：參考文獻

1. L. Lovász, *Kneser’s Conjecture, Chromatic Number, and Homotopy*, Journal of Combinatorial Theory, Series A, 25(3), 319–324, 1978.
2. A. Schrijver, *Vertex-Critical Subgraphs of Kneser Graphs*, Nieuw Archief voor Wiskunde, 26, 454–461, 1978.
3. J. Matoušek, *A Combinatorial Proof of Kneser’s Conjecture*, Combinatorica, 24, 163–170, 2004.
4. H. R. Daneshpajouh and J. Osztényi, *On the Neighborhood Complex of s-Stable Kneser Graphs*, 2019 preprint.
5. A. Bickle, *Intersecting Families of 3-Sets*, Australasian Journal of Combinatorics, 93(1), 216–223, 2025.
6. A. Parker, *Problems in Extremal Combinatorics*, doctoral dissertation, Iowa State University, 2026.
7. W.-C. Chen, A. Parker and S. Zerbib, *Chromatic Number of 3-Stable Kneser Graphs*, public seminar abstract, 2026.
8. S. Zerbib, W.-C. Chen and A. Parker, *The Chromatic Number of s-Stable Kneser Graphs*, conference abstract, 2026.

---

# 附錄 E：研究誠信聲明

1. 本文保留錯誤與修正，不將路徑重寫成無失敗的線性敘事。
2. 最後定理不宣稱世界首證。
3. 2019、2025、2026 文獻中的既有成果已被明確區分。
4. exact verifier 只證明其形式化範圍內的有限命題。
5. 解析容量引理仍應接受獨立同行逐型審查。
6. 模型是否在某一步回憶了既有結構，不能僅由輸出完全判定。
7. 本文主要貢獻是研究路徑、狀態壓縮與自我修正機制的可觀測化。
