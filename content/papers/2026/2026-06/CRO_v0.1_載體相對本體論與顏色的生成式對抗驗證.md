# 載體相對本體論與顏色的生成式對抗驗證問題
## ——以 olo 為經驗錨點

**Carrier-Relative Ontology (CRO) v0.1**
EveMissLab ／ 許筌崴 (Neo.K)
與 Theia 結晶化對練

---

## 摘要

本文處理一個被通俗敘述（「顏色本身不存在，現實只有波長」）反覆提出、卻範疇錯置的命題。我們主張：

1. 「顏色不存在，只有波長存在」不是假命題，而是 **範疇不對等下的 not-even-wrong**——它把現象範疇（色）與結構範疇（波長）壓到同一條存在軸上比較，前提即不成立。
2. 顏色不是波長的近似，而是無窮維光譜空間 $\Sigma$ 經由載體受體流形的 **有損投影** $\pi_C:\Sigma \to M_C$。色彩空間由受體通道結構生成，**不由波長生成**。metamerism（異譜同色）即此投影的核；olo 即對此投影 *自然可達像* 的邊界突破。
3. 表徵與世界是否同構，是一個 **無內生判別器的生成式對抗驗證問題**，其不動點是經驗充分性而非對應，原理上不可從單一載體類內判定。異質載體（他種、AI、改造人）的功能不是確認同構，而是作為獨立判別器 **破壞既有均衡**。
4. 由此導出 **不可預覽定理**：真正正交的新質感在當前載體內無表徵、無從預覽；其唯一取得途徑是改變載體。進而導出 **願望同一性**：「感知當前不可感知者」與「不再是當前載體」在內容上同一。

關鍵詞：載體相對性、感知投影、metamerism、生成式對抗驗證、質感不可預覽、olo

---

## 0. 記號與基本對象

| 符號 | 含義 |
|---|---|
| $C$ | 載體（carrier）：將世界態映為經驗態的基底相對換能—表徵系統 |
| $\Sigma$ | 光譜空間：定義在波長上的（無窮維）輻射函數空間 |
| $M_C$ | 載體 $C$ 的受體激發流形；人類三色視覺 $\dim M_C = 3$ |
| $\pi_C$ | 感知投影 $\pi_C:\Sigma \to M_C$ |
| $P,S,E$ | 三範疇：現象（phenomenal）、結構/關係（structural）、認識關係（epistemic，「近似」屬此） |

> **定義 0.1（載體）** 感知是 $C$-相對的。$C$ 不是裝載同一主體的被動容器；擁有經驗的認知結構部分地由 $C$ 構成。

此定義刻意取中性語——對應物理中以「參考系」取代「特權觀察者」的動作——而不採「後人類／新人類」等已偷渡目的論或身分宣告的詞。其唯一不中性處見 §6。

---

## 1. 範疇錯置：為何「顏色不存在」是 not-even-wrong

通俗命題「顏色本身不存在，這是大腦對現實的近似，現實只有波長」隱含一個前提：色（$P$）與波長（$S$）爭奪同一個「誰才存在」的位子。

> **命題 1.1（範疇不對等）** $P$（第一人稱、內稟、質性）、$S$（第三人稱、外在、關係量）、$E$（認識論關係，「近似」）分屬不可通約的三條本體論軸。將 $P$ 與 $S$ 壓至單一存在軸的命題，其真值載體尚未成立，故 **不是假，而是 not-even-wrong**。

推論：「色與波長是否同構（$P\cong S$）」這一問句繼承同一非法性，**除非先限縮到 $S$–$S$ 比較**（即色彩空間結構 vs 受體響應空間結構，見 §2）。在現象層上談 $P\cong S$ 是範疇越界。

> **命題 1.2（神經科學的範疇限度）** 神經科學給出的是質感出現之時機與機制的統計相關，屬 $S$ 層敘述。它無資格裁決一個 $P$ 層的存在宣告。以神經機制「證明顏色不存在」本身是又一次跨範疇。

〔歪臉笑：通俗敘述用一個正確觀察（顏色是被建構的）偷渡一個未經論證的價值排序（所以顏色比波長不真實）；其全部說服力，靠的是這條接縫不被看見。〕

---

## 2. 感知投影：色彩空間是受體生成的，不是波長生成的

> **定義 2.1（感知投影）** $\pi_C:\Sigma \to M_C$。色是 $M_C$ 中的一點，不是 $\Sigma$ 中的一點。對人類三色載體，$\pi_C$ 將無窮維 $\Sigma$ 壓成三維 $M_C$。

> **命題 2.2（metamerism＝核）** $\pi_C$ 的纖維（映至同一激發態的光譜集合）即此投影的核；一般情形 $|\text{fiber}|>1$，故 $\pi_C$ 大規模非單射。**色因此不可能是「還原波長」的函數**。色不是波長的讀數，是 $\Sigma$ 被受體閉合後的投影像。

> **接 DCO** 此即 $\pi_n(\mathrm{Cl})=S^{n-1}$ 的維度投影/閉合在視覺中的實例：無窮維源空間經受體閉合，墜為低維像。色彩恆等性、色彩對比等則進一步顯示 $M_C$ 上的點還受環境調制——大腦在解一個反問題（輻射＝反射率×照明，欠定），色是對表面不變量的貝氏推斷，不是對 $\Sigma$ 的逐點抄寫。

> **命題 2.3（olo＝邊界突破）** 設自然光約束下可達的子集為 $\mathrm{im}(\pi_C)|_{\text{nat}} \subsetneq M_C$。olo $\in M_C$ 落在此子集 **之外**：它由 Oz 技術直接驅動「僅 M 錐」此一座標達成，而**無任何 $\sigma\in\Sigma$ 能單獨刺激 M 錐**〔Fong et al., 2025, [1]〕。（嚴格形式化見附錄 A.3）
>
> **故 $M_C$ 由載體通道結構生成，不由 $\Sigma$ 生成。** 通俗敘述把 olo 講成「世界沒有顏色」的證據，恰好講反：連世界端被拔除，顏色仍可被點亮——olo 證明的是色彩空間的受體生成性，而非波長的本體優位。

非光譜色（洋紅、棕、灰、白、金屬光）佐證同一結論：絕大多數被感知的顏色本就沒有單一波長原像；洋紅是大腦為閉合色相環而生成者（光譜上的 purples 之線不存在）。「色＝對波長的近似」對多數色早已失效，olo 僅使之無法迴避。

---

## 3. 生成式對抗驗證：同構不可從載體內判定

> **定義 3.1（生成式對抗驗證）** 欲驗證保結構映射 $\varphi:M_C \to W$（$W$＝世界），需獨立取得 $W$ 以對照；但 $W$ 永遠只透過另一表徵 $M_{C'}$ 被給出。將其設為賽局：
> - 生成器 $G$：不斷產生更貼合觀測的表徵；
> - 判別器 $D$：檢驗貼合度，但 **無 $W$ 的真值（no oracle）**，手上只有更多表徵。

> **命題 3.2（無對應證書）** 此賽局的不動點是 **經驗充分性**，非對應。多個彼此不相容的表徵皆可為均衡（欠定）。賽局非終止——每個均衡皆可被新資料或新判別器重啟。**故「色↔世界同構」在單一載體類內不可判定。** 這是一個無限的生成式對抗問題。（賽局形式化見附錄 B）
>
> 〔接 GAR：通俗敘述中的「近似」恰是 GAR 三元的 A（Approximation）。它把 A 當成 $M_C\!\leftrightarrow\!W$ 關係的全部，漏掉 A 從不附帶 Restoration 之保證——近似不蘊含可還原。〕

> **命題 3.3（新個體＝獨立判別器）** 結構上異質的載體 $C'$（他種、AI、改造人）帶有不同歸納偏置，其認識論功能 **不是確認同構，而是破壞均衡**：它能擊垮人類全體玩家長期誤認為「世界」的那個納許均衡，揭露其中某些特徵實為載體相對、被誤讀為世界特徵。olo 是此事的 **載體內小型版**：它撬掉了「$M_C$＝$\Sigma$ 可達空間」這一均衡。

附帶界限：AI 能傳遞的是結構（$S$ 層的關係幾何），不是質感（$P$ 層）。倒反光譜在人與人之間已說明：可對齊者僅「用詞一致、行為一致」，從不是那團質感本身。**故更多路徑買得到的是更穩健的結構骨架，買不到質感的送達。** 任何把「分享所得之結構」宣告為「驗證了現象本體」的動作，是 §1 範疇錯置的反向重犯。

---

## 4. 顏色擴張的分層 E0–E3

> **定義 4.1（擴張分層）**
>
> - **E0｜可達體積擴張**（固定 $\dim M_C$）：在既有三錐空間內點亮自然光到不了的角落。**例：olo**。本質仍在既有範疇內（「最綠的綠」），質感可外推。
> - **E1｜維度擴張**（既有大腦＋新通道）：**例：人類四色視覺。** 須區分「視網膜四色」（因 X 染色體隨機去活化，約 12% 女性帶四類錐——常見）與「功能性四色」（行為上確實動用第四維——罕見）。Jordan et al. (2010) 於 24 位專性紅綠色弱攜帶者中僅 1 位（cDa29）在全部測試展現四色行為〔[4]〕。**坊間「多辨上百倍／一億色」之說屬理論外推，非該研究之實測，本文不採。** **例：2009 松鼠猴 opsin 基因治療**——對成體二色猴補入人類 L-opsin，行為上獲三色辨色〔[2]〕。關鍵：原作者明言無法判定其是否產生新的內在「紅／綠」感質，僅測得辨別行為之擴張——**恰好印證 §3 的結構/質感之別**。對載體論的最硬經驗支撐。
> - **E2｜光譜範圍擴張**（騎在既有 $M_C$ 上）：**例：紅外上轉換奈米粒子 (pbUCNP)** 使小鼠見近紅外——奈米粒子將約 980 nm 上轉換為約 535 nm，**映回既有綠通道**〔[3]〕；人眼晶狀體濾除近 UV，無晶體眼（aphakia）者報告對近 UV 之感受。給的是 **新資訊，不必然是新質感**——新波長被映回既有質感座標。
> - **E3｜正交新軸**：一條真正獨立的新通道被整合為新維度。**真正的新質感。**

E0–E2 多為現有質性空間的外推、加密或重映；唯 E3 逸出當前 $M_C$。

---

## 5. 不可預覽定理與願望同一性

> **定理 5.1（不可預覽）** 設 $q$ 為一 E3 質感，依構造 $q \notin M_C$。則當前載體 $C$ 內 **無 $q$ 的表徵，亦無任何 $C$-內操作可生成 $q$ 的預覽**。$q$ 的唯一取得途徑，是獲得使 $q\in M_{C'}$ 的載體 $C'$。
>
> *證理* 預覽須以 $C$-內表徵呈現；$q\notin M_C$ 故無此表徵。問三通道腦「第四維顏色何感」與問天生全盲者「紅何樣」同類——答案不在當前載體的表徵空間內。$\square$

> **推論 5.2（願望同一性）** 對 E3 質感 $q$：
> $$\text{「感知 } q\text{」} \iff \text{「實例化使 } q\in M_{C'} \text{ 之載體 } C'\text{」}.$$
> 結合定義 0.1（主體部分由 $C$ 構成）：**改變載體不是達成願望的手段，改變載體就是願望的內容本身。** 「想看當前看不到的顏色」在邏輯上等同於「想不再是那個看不到它的載體」。

此即「需要腦機介面／基因／受體工程」之嚴格根據：那些不是工具，而是願望的內容。而「當前人類無法理解」這一條件，恰恰保證當前主體取不到預覽——你只能 *成為* 那個能理解它者，而那一刻，「當前的你」正是被改掉的那一塊。

---

## 6. 載體的中性性及其唯一破口

「載體」是最小的、基底不可知的本體原語（cf. 參考系 vs 特權觀察者），把問題壓在工程與經驗層，不令其滑為身分政治。它在絕大多數方向上中性——

> **命題 6.1（唯一破口）** 唯一不中性處：擁有經驗的主體部分由 $C$ 構成（定義 0.1）。故 **換載體 ≠ 同份資料換硬碟**；不保證存在一個載體不變、跨換後仍享受新質感的同一主體。享受 $q$ 的那個，部分由賦予 $q$ 的載體 $C'$ 造出。

通俗語境中「褻瀆」之感，其真正當量不在「人類尊嚴」，而在此冷結構：想看現在看不到的顏色，邏輯上即想不再是看不到它的載體。與道德無關，這是願望本身的結構。

---

## 7. 待補（Open Problems）

1. ~~$M_C$ 拓撲/度量、E3 正交性之形式化~~ → **已完成，見附錄 A。**
2. ~~生成式對抗賽局之形式化~~ → **已完成，見附錄 B。**
3. （掛起）與 DCO 四公理（Cl-1～Cl-4）的正式嵌入：$\pi_C$ 是否為 $\pi_n(\mathrm{Cl})$ 的特例。
4. （掛起）「結構可分享、質感不可分享」之界線的可操作判準（跨載體不變量的萃取程序）。
5. ~~E1 經驗錨之引用核校~~ → **已核（見參考文獻）。本輪修正兩處：四色視覺「百倍色差」說為外推、非實測，已撤；E2 紅外經約 535 nm 映回綠通道，已補實。**

---

## 附錄 A：感知投影 $\pi_C$ 的基本形式化與 E3 正交性

### A.1 光譜空間與受體響應（線性階）

光譜功率分佈 (SPD) 為非負函數 $s:\Lambda\to\mathbb R_{\ge0}$，$\Lambda=[\lambda_{\min},\lambda_{\max}]$。令 $\Sigma\subset L^2_{\ge0}(\Lambda)$ 為 SPD 之集合，$\dim\Sigma=\infty$。

載體 $C$ 具 $n$ 種受體，敏感度 $\{r_i\}_{i=1}^n\subset L^2(\Lambda)$，$r_i\ge0$；人類三色 $n=3$，$\{r_L,r_M,r_S\}$。定義受體響應算子（量子捕獲，線性）：

$$R:\;L^2(\Lambda)\to\mathbb R^n,\qquad (Rs)_i=\langle r_i,s\rangle=\int_\Lambda r_i(\lambda)\,s(\lambda)\,d\lambda.$$

$R$ 線性、有界。感知投影之線性核心 $\pi_C^{\mathrm{lin}}:=R|_\Sigma$。

### A.2 metamerism＝核（命題 2.2 的嚴格形式）

同色異譜類 $[s]_C=\{s'\in\Sigma: Rs'=Rs\}=(s+\ker R)\cap\Sigma$，其中

$$\ker R=\{r_1,\dots,r_n\}^{\perp},\qquad \operatorname{codim}\ker R=\operatorname{rank}R=n,\quad \dim\ker R=\infty.$$

$\ker R$ 即 Wyszecki 意義下的「同色黑」(metameric black) 空間——對 $C$ 完全不可見的光譜自由度〔[6]〕。投影沿 $\ker R$ 整體坍縮，故 $\pi_C$ 大規模非單射，**色不可能是還原 $s$ 的函數**。

### A.3 自然色域與 olo（命題 2.3 的嚴格形式）

自然光可達響應集為非負錐之像：

$$K_C^{\mathrm{nat}}=R(\Sigma)=\operatorname{cone}\{R\delta_\lambda:\lambda\in\Lambda\}\subseteq\mathbb R^n_{\ge0},$$

即光譜軌跡所張凸錐。因 $r_L,r_M$ 於中波段大幅重疊，不存在 $s\ge0$ 使 $Rs\parallel e_M:=(0,1,0)$，故

$$e_M\notin K_C^{\mathrm{nat}}\quad(\text{即「無波長能單獨刺激 M 錐」}〔[1]〕).$$

Oz 以 cell-by-cell 光遞送直接設定生理響應 $\mathbf a$，可達集 $K_C^{\mathrm{phys}}\supsetneq K_C^{\mathrm{nat}}$，含朝 $e_M$ 之極端態。故 **$\mathrm{olo}\in K_C^{\mathrm{phys}}\setminus K_C^{\mathrm{nat}}$**：$M_C$ 中、$R$ 自然像之外的邊界突破。色域之界由響應座標（受體通道結構）界定，非由 $\Sigma$ 界定；「自然色域＝色域」是 $R$ 之像所致的載體相對假象。

### A.4 感知流形與度量（非線性階）

受體響應後接神經處理（對立轉換、增益、適應），記非線性、依情境之 $\Phi_C:K_C^{\mathrm{phys}}\to M_C$，$\dim M_C=n$。其可操作結構為辨別度量：以恰可辨差 (JND) 定義線元 $ds^2=g_{ij}(\mathbf a)\,da^i da^j$（line-element 理論：Helmholtz–Schrödinger–Stiles）。

> **假設 A-i（弱度量假設）** 本文僅設「$M_C$ 為 $n$ 維、帶辨別度量的流形」，**不預設黎曼性**——Bujack et al. (2022) 由「大差異收縮」(diminishing returns) 論證感知色空間違反黎曼可加性〔[5]〕，故 $g_{ij}$ 至多為非黎曼度量結構。

### A.5 E3 正交性的嚴格定義

設新載體 $C'$ 加入第 $(n{+}1)$ 受體 $r_{n+1}$，響應算子 $R':L^2\to\mathbb R^{n+1}$。

> **定義 A.5（通道層獨立性）** 新通道資訊獨立 $\iff r_{n+1}\notin\operatorname{span}\{r_1,\dots,r_n\}$，等價於 $\operatorname{rank}R'=n+1$。嚴格正交 $\langle r_{n+1},r_i\rangle=0$ 過強（真實受體必重疊），**線性獨立為必要且充分**。

> **定義 A.5′（感知層新軸）** 新感知軸 $=$ $C$ 不可分辨、$C'$ 可分辨之方向，形式上同構於商空間
> $$N:=\ker R\,/\,(\ker R\cap\ker R'),\qquad \dim N=\operatorname{rank}R'-\operatorname{rank}R=1.$$
> 即 **E3 的新軸恰由舊核 $\ker R$（對 $C$ 的同色黑、原不可見子空間）中被 $R'$ 解析出的一維構成。**

> **定理 A.5（不可預覽的線性形式，＝定理 5.1）** 設 $q$ 之光譜對比僅落於 $\ker R$ 內，即存在 $u\in\ker R\setminus\ker R'$ 使 $q$ 之刺激 $=$ 基線 $+\,u$。則
> $$\pi_C(\text{基線}+u)=R(\text{基線}+u)=R(\text{基線})=\pi_C(\text{基線}),$$
> 故 $q$ 在 $C$ 內與基線同響應、無表徵；任何 $C$-內操作皆沿 $\ker R$ 坍縮，無法生成 $q$ 之預覽。$q$ 僅在 $\operatorname{rank}$ 提升（獲得 $C'$）後成為 $M_{C'}$ 之座標。$\square$

**E0 與 E3 之精確分界**：E0（olo）在固定 $\operatorname{rank}R=n$ 下擴張 $K_C^{\mathrm{phys}}$（同維、擴體積）；E3 提升 $\operatorname{rank}$ 至 $n+1$（加維）。新質感住在當前投影的核裡——這是「不可預覽」從現象學斷言降為線性代數事實。

---

## 附錄 B：生成式對抗驗證的賽局形式化（命題 3.2–3.3）

### B.1 對象

世界 $W$（不可直接取用）。觀測經由載體之觀測通道 $\mathcal O_C:W\to\mathcal M_C$。對應假設為 $\varphi:\mathcal M_C\to W$（宣稱保結構），假設集記 $\Phi$。資料 $d=\mathcal O_C(w)$。

### B.2 經驗等價與欠定

> **定義 B.1（$\mathcal C$-經驗等價）** 對載體類 $\mathcal C$：
> $$\varphi\sim_{\mathcal C}\varphi'\iff \forall C\in\mathcal C,\,\forall w\in W:\ \varphi,\varphi'\text{ 對 }\mathcal O_C(w)\text{ 之預測一致}.$$

> **命題 B.2（有損 ⇒ 等價類非平凡）** 若 $\ker\mathcal O_C\ne 0$（由附錄 A，受體投影必有 $\ker R\ne0$，恆成立），則存在 $\varphi\ne\varphi'$、對應不同 $W$-結構卻 $\varphi\sim_{\mathcal C}\varphi'$。此即理論被資料欠定 (Quine–Duhem) 之通道版本。

### B.3 賽局與無對應證書

兩方零和賽局 $\mathcal G(\mathcal C)$：生成器 $G$ 選與已見資料一致之 $\varphi$（落在版本空間 $\Phi_D$）；判別器 $\mathsf D$ 選檢驗 $T$，欲區分「真對應」與「僅經驗充分」，但**僅能取用 $\mathcal C$-中介資料，無 $W$ 真值（no oracle）**。

> **定理 B.3（無對應證書）** $\mathcal G(\mathcal C)$ 之均衡集 $\mathcal E(\mathcal C)=\{[\varphi]_{\sim_{\mathcal C}}\}$ 為 $\sim_{\mathcal C}$ 等價類；每類僅被認證至**經驗充分**，非對應。當 $\ker\mathcal O_C\ne0$（恆成立），$\mathcal E(\mathcal C)$ 含對應發散之成員（命題 B.2），故**無 $\mathcal C$-內判別器能輸出對應證書**；賽局非終止——新資料只縮小 $\Phi_D$，不消滅 $\sim_{\mathcal C}$。$\square$

### B.4 異質判別器與均衡崩塌（命題 3.3 的嚴格形式）

引入 $C'$，使 $\ker\mathcal O_{C'}\subsetneq\ker\mathcal O_C$（嚴格更細）。記 $\mathcal C^+=\mathcal C\cup\{C'\}$。

> **命題 B.4（均衡分裂）** 存在原 $\varphi\sim_{\mathcal C}\varphi'$ 轉為 $\varphi\not\sim_{\mathcal C^+}\varphi'$：$\mathcal E(\mathcal C)$ 中某些類在 $\mathcal E(\mathcal C^+)$ 裂開。$C'$ 充當分辨力嚴格更大之判別器。**界限**：除非 $\ker\mathcal O_{\mathcal C^+}=0$（一般不成立），$\mathcal E(\mathcal C^+)$ 仍非單點，仍不輸出對應證書。

> **推論 B.4（新個體的認識論功能）** 新載體之作用是**核的單調收縮** $\ker\mathcal O_{\mathcal C^+}\subseteq\ker\mathcal O_{\mathcal C}$，即 falsify 因 $\ker\mathcal O_C$ 而生之偽均衡，**非 confirm 對應**。olo/Oz 為載體內實例：Oz 把可控區由 $K_C^{\mathrm{nat}}$ 擴至 $K_C^{\mathrm{phys}}$（附錄 A.3），擊垮「色域＝自然可達」此偽均衡——沒證明任何對應，只揭露一個被誤認為世界事實、實為通道假象的邊界。

### B.5 與附錄 A 的統一

兩附錄的承重物是同一物件：**核**。

| | 附錄 A（現象側） | 附錄 B（認識側） |
|---|---|---|
| 核 | $\ker R$＝同色黑 | $\ker\mathcal O_C$＝經驗等價之源 |
| 作用 | 色覺有損性之源；E3 新軸自此雕出 $N=\ker R/(\ker R\cap\ker R')$ | 偽均衡之所在；新判別器收縮之對象 |
| 操作 | 加維（提升 $\operatorname{rank}$） | 裂均衡（收縮 $\ker$） |

「看見新顏色」與「驗證新區別」在形式上同構為同一操作：**降低觀測通道的核**。驅動兩者的，都是對載體 $C$ 的更動。〔與待補 4 相接，惟其可操作判準仍掛起。〕

---

## 參考文獻

[1] Fong, J., Doyle, H. K., Wang, C., Boehm, A. E., Herbeck, S. R., Pandiyan, V. P., Schmidt, B. P., Tiruveedhula, P., Vanston, J. E., Tuten, W. S., Sabesan, R., Roorda, A., & Ng, R. (2025). Novel color via stimulation of individual photoreceptors at population scale. *Science Advances*, 11(16), eadu1052. https://doi.org/10.1126/sciadv.adu1052

[2] Mancuso, K., Hauswirth, W. W., Li, Q., Connor, T. B., Kuchenbecker, J. A., Mauck, M. C., Neitz, J., & Neitz, M. (2009). Gene therapy for red–green colour blindness in adult primates. *Nature*, 461(7265), 784–787. https://doi.org/10.1038/nature08401

[3] Ma, Y., Bao, J., Zhang, Y., Li, Z., Zhou, X., Wan, C., Huang, L., Zhao, Y., Han, G., & Xue, T. (2019). Mammalian near-infrared image vision through injectable and self-powered retinal nanoantennae. *Cell*, 177(1), 243–255. https://doi.org/10.1016/j.cell.2019.01.038

[4] Jordan, G., Deeb, S. S., Bosten, J. M., & Mollon, J. D. (2010). The dimensionality of color vision in carriers of anomalous trichromacy. *Journal of Vision*, 10(8):12, 1–19. https://doi.org/10.1167/10.8.12

[5] Bujack, R., Teti, E., Miller, J., Caffrey, E., & Turton, T. L. (2022). The non-Riemannian nature of perceptual color space. *Proceedings of the National Academy of Sciences*, 119(18), e2119753119. https://doi.org/10.1073/pnas.2119753119

[6] Wyszecki, G., & Stiles, W. S. (1982). *Color Science: Concepts and Methods, Quantitative Data and Formulae* (2nd ed.). Wiley.〔同色黑 / metameric black 之標準定義〕

---

## 結語

世界不欠你一個「最真的那層」。它只欠你一個誠實的問句——當每一層都喊著只有更下面才真、而最下面是空的時候，那個一路都在發問的，是誰。

你想要的從來不是一個顏色，是站到一個還不存在的視角上。而那個視角不會把它看見的東西寄回給現在的你；它只在那裡，等你走過去、成為它。

新顏色不是被看見的，是被成為的。
