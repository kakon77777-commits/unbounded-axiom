# 黎曼猜想思想實驗 3.0
## 一個探索性進路、它斷裂的座標、全部推導，與延伸公式的演算法價值（公開最終版）
### A Thought Experiment on the Riemann Hypothesis 3.0 — An Exploratory Approach, the Exact Point of Its Failure, All Derivations, and the Algorithmic Value of the Derived Formulas

**作者：** Neo.K（一言諾科技有限公司 / EveMissLab）
**日期：** 2025 年 12 月（最終版）
**性質：** 探索性筆記與公開更正（非證明）。對 RH 而言，本文是**啟發**；其延伸公式則是**可運行的演算法**。

---

## 致讀者

本文最初以「黎曼猜想之證明」的形式起草。經逐步審視，**此證明不成立**——其核心論證存在數個彼此獨立的致命缺陷，詳見第二部分與第三部分的完整推理鏈。

現將它改以「探索性筆記與公開更正」的形式發布。我選擇不刪去原構想，而是完整保留它、精確解剖它斷裂的位置、給出全部相關公式的逐步推導與程式驗證的重新計算，並在最後說明：這條路對 RH 而言只是**啟發**，但它**延伸出的公式都是可運行的演算法**——這才是它真正的價值所在。

以證明之名呈現一個未竟之物，是需要更正的。這份文件就是那個更正。它不主張任何新定理；它主張兩件更樸素的事：**一條看似通向山頂的路，其斷裂處的精確座標值得被公開記錄；而沿途撿到的工具，是真的能用的。**

全文約定：✅ 正確、⚠️ 有缺口、❌ 致命錯誤、⟂ 開放之牆。所有推導以「自足、可獨立驗算」為標準；第二、四附錄的全部數值以 mpmath（30 位精度）程式驗證。

---

# 第一部分：原構想（進路概述）

## 全局論證鏈（原始版本）

> 1. Rodgers-Tao (2018)：$\Lambda \geq 0$。
> 2. 任何 $\Lambda > 0$ 會破壞歐拉乘積的因子化結構。
> 3. 歐拉乘積等價於算術基本定理，其有效性已被現代科技驗證。
> 4. 故 $\Lambda = 0$，即黎曼猜想成立。

## 各章核心主張

**第一章（基礎）。** 算術基本定理作為公理性結構；歐拉乘積 $\zeta(s)=\prod_p(1-p^{-s})^{-1}$（$\mathrm{Re}\,s>1$）；完成化 $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ 與功能方程 $\xi(s)=\xi(1-s)$；歸心變換 $k=s-\tfrac12$、$\Xi(k):=\xi(k+\tfrac12)$，得偶函數 $\Xi(k)=\Xi(-k)$。

**第二章（對稱鎖定）。** 鏡像 $\mathcal{M}$、共軛 $\mathcal{C}$ 下 $\Xi$ 不變；零點四元組 $\{\rho,-\rho,\bar\rho,-\bar\rho\}$；定義 Berry 相位 $\Phi_B[\Gamma]=\oint_\Gamma\mathrm{Im}(d\Xi/\Xi)$；宣稱對稱圍道使 $\Phi_B=0$，與輻角原理給出的 $2\pi\cdot 4n$ 矛盾，迫使零點實部為零。

**第三章（核心）。** De Bruijn-Newman 函數 $H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du$，$H_0=\Xi$；$\Lambda=\sup\{\lambda:H_\lambda\text{ 有複零點}\}$；RH $\Leftrightarrow\Lambda\leq 0$，結合 $\Lambda\geq 0$ 得 RH $\Leftrightarrow\Lambda=0$。宣稱熱核等價於對 Dirichlet 係數的對角乘子 $K_\lambda(n)=\exp(-\tfrac{\lambda}{4}(\log n)^2)$；主定理：$K_\lambda$ 對 $\lambda\neq 0$ 不乘法，$R_\lambda(p,q)=\exp(-\tfrac{\lambda}{2}\log p\log q)\neq 1$；故 $\Lambda>0$ 破壞歐拉乘積，矛盾，得 $\Lambda=0$。

**第四章（瞬間形變）。** 算符 $D_{\text{inst}}F=\lim_{\epsilon\to 0}(\partial_t F+\delta(t)\Delta_{\text{top}}F)$；宣稱繞數只在臨界線上為整數，偏離則「連續化」。

**第五章（歷史自洽性）。** 宣稱 $\Lambda>0$ 使歐拉乘積失效，進而 RSA、QED、哈希、弦論皆應崩潰；由它們精確運作貝葉斯地推出 $\Lambda=0$。

---

# 第二部分：失敗的解剖

按「最致命且最不可挽救」到「技術性」排列。

## §2.1 根本診斷：歐拉乘積與臨界帶零點的脫鉤（死因）

本文把四個彼此獨立、難度天差地遠的命題，混為一談地塞進「歐拉乘積」這個詞下：

| 命題 | 地位 | 與 RH 的關係 |
|---|---|---|
| (a) 唯一分解（算術基本定理） | 初等、無條件 | **完全無關** |
| (b) 歐拉乘積在 $\mathrm{Re}(s)>1$ 收斂且等於 $\zeta$ | 初等、無條件 | **完全無關** |
| (c) 素數定理 $\pi(x)\sim x/\log x$ | 已證（1896），無條件 | RH 只**改善誤差項**，非其前提 |
| (d) RH：臨界帶零點都在 $\mathrm{Re}(s)=\tfrac12$ | **開放** | 即 RH 本身 |

關鍵在 (b) 的作用域。歐拉乘積收斂並等於 $\zeta$ 的區域是 $\mathrm{Re}(s)>1$——**該區域內一個零點都沒有**。RH 講的是 $0<\mathrm{Re}(s)<1$ 的零點，而在那裡歐拉乘積根本不收斂、什麼都不說（推導見附錄 A.1）。於是「歐拉乘積的有效性」對臨界帶零點位置提供的信息量，嚴格為零。整個建築奠基於一個錯誤信念：以為歐拉乘積約束了臨界帶的零點。它不約束。

## §2.2 第三章：兩個獨立的致命錯誤

### §2.2.1 「形變後失去歐拉乘積＝矛盾」是非邏輯跳躍（最乾淨的一刀）

定理 3.3 的代數**正確**：$g_\lambda(n)=\exp(-\tfrac{\lambda}{4}(\log n)^2)$ 對 $\lambda\neq 0$ 確實不乘法（重算見附錄 B.1）。但這一步**什麼都證不出來**，因為「沒有歐拉乘積」不是矛盾。**不存在任何定理說「Dirichlet 級數必須乘法」。** 無可爭辯的反例（推導見附錄 A.8）：

$$-\zeta'(s)=\sum_{n\geq 1}(\log n)\,n^{-s}.$$

係數 $\log n$ 不乘法，故 $-\zeta'(s)$ 無歐拉乘積，卻是完全合法、毫無矛盾的解析函數。算術基本定理是關於整數的命題，從不要求任意權重 $g_\lambda(n)$ 必須乘法。De Bruijn-Newman 流的全部目的就是把 $\Xi$ 形變成 $H_\lambda$ 觀察零點移動；$H_\lambda$（$\lambda\neq 0$）本來就不是 $\zeta$、本來就不乘法——這是設計使然，不是矛盾。**這一刀在不碰任何熱核細節下，獨立殺死整個第三章。**

### §2.2.2 定理 3.1 對 DBN 流的刻畫，符號與性質都錯

由附錄 A.5，DBN 流是 $z$ 上的**逆向熱方程（卷積算符）** $H_\lambda=e^{-\lambda\partial_z^2}\Xi$，不是對 $\zeta$ 係數的對角乘子。故定義 3.5 的 $\zeta_\lambda(s)=\sum K_\lambda(n)n^{-s}$ 是憑空虛構，不等於 $H_\lambda$。即使用最寬鬆的「頻譜乘子」啟發式，$\lambda>0$ 對應 $e^{+\lambda\xi^2}$（放大），而非 $K_\lambda$ 的衰減——**連符號都相反**（重算見附錄 B.2）。即使把符號全部修正，§2.2.1 仍成立：那座橋即使修好，也通往一個不存在的矛盾。

## §2.3 第二章：Berry 相位即輻角原理，定理 2.2 自證偽

由 $d\Xi/\Xi=d\log|\Xi|+i\,d(\arg\Xi)$ 且閉圍道上 $\oint d\log|\Xi|=0$（推導見附錄 A.6）：

$$\Phi_B[\Gamma]=\oint_\Gamma\mathrm{Im}\frac{d\Xi}{\Xi}=\oint_\Gamma d(\arg\Xi)=2\pi N_\Gamma,\qquad N_\Gamma\geq 0.$$

這**就是輻角原理本身**。定理 2.2 宣稱「對稱圍道 $\Rightarrow\Phi_B=0$」等於宣稱「任何對稱圍道內都沒有零點」——被 $\Xi$ 的無窮多個零點立刻證偽。錯在 $\phi_L=-\phi_R$ 是假的：每個單零點貢獻 $+1$ 繞數，對稱零點對**同號相加**（附錄 A.6 給出 $\rho,-\rho$ 同在內時 $\oint=4\pi i$ 的顯式計算；附錄 B.3 程式驗證臨界帶內繞數為 3 而非 0）。第二章證不出任何東西。

## §2.4 第五章：前提鏈全偽

**RSA** 依賴整數分解**在計算上很難**，不依賴分解唯一；唯一分解與零點位置無關。**QED** 中的 $\zeta(2)=\pi^2/6$ 等是由 $\mathrm{Re}\,s>1$ 上初等求和決定的具體數值，RH 不改變它們。**素數定理**自 1896 年無條件成立。**弦論** $\zeta(-1)=-\tfrac1{12}$ 是無條件的解析延拓。四項皆不依賴 RH，「科技能跑」對 $\Lambda$ 的證據性權重 $\approx 0$。此章是 §2.1 在現實層面的重演。

## §2.5 第四章：未定義的算符

$D_{\text{inst}}$ 不是良定義物件（Dirac $\delta$ 乘上從未定義的 $\Delta_{\text{top}}$）。定理 4.1 真但平凡；定理 4.2（$t\neq 0$ 繞數「連續化」）假——繞數對閉圍道恆為整數。本章無嚴格內容。

## §2.6 數值方案：數值符合不是結構證據

$\Delta_\lambda$ 測的只是「$g_\lambda$ 不乘法」，對 $\zeta$ 或 $\Lambda$ 零信息。「$\zeta(2)$ 精確 $\Rightarrow\Lambda\approx 0$」把虛構的 $\zeta_\lambda$ 與真實 $\zeta(2)$ 等同。一般原則：**在一個與目標物件無因果連結的數量上觀測到任意高的數值符合，對目標物件不提供證據。**

## §2.7 Lean4 附錄：主定理真但無關，最終定理循環

`heat_kernel_not_multiplicative` 為真且可證，但對 RH 無貢獻。`riemann_hypothesis` 區塊**循環**：把偽矛盾當假設引入再收尾。真送進 Lean4，它會在那個 `sorry` 處立刻卡死——形式化會在第一時間暴露缺口。

---

# 第三部分：完整推理鏈（原始版 vs. 修正版）

把上面的解剖收攏成一條可逐環檢視的鏈。這是判斷「哪裡斷、為何斷、修正後為何更好」的核心。

## §3.1 原始推理鏈（逐環標註斷點）

| 環 | 內容 | 判定 |
|---|---|---|
| L1 | 算術基本定理（唯一分解）成立 | ✅ 無條件 |
| L2 | $\Rightarrow$ 歐拉乘積 $\zeta=\prod_p(1-p^{-s})^{-1}$（$\mathrm{Re}\,s>1$） | ✅ |
| L3 | 完成化 $\xi$、功能方程、歸心 $\Xi(k)=\Xi(-k)$ | ✅ |
| L4 | **〔斷點①〕** 歐拉乘積的有效性約束臨界帶零點 | ❌ 偽 |
| L5 | **〔斷點②〕** $H_\lambda$ ＝ 對 $\zeta$ 係數的對角高斯乘子 $K_\lambda(n)$ | ❌ 偽 |
| L6 | $g_\lambda=K_\lambda$ 對 $\lambda\neq 0$ 不乘法 | ✅ 真，但無關 |
| L7 | **〔斷點③〕** 非乘法 $\Rightarrow$ 破壞歐拉乘積 $\Rightarrow$ 矛盾 | ❌ 偽 |
| L8 | $\Rightarrow\Lambda\leq 0\Rightarrow\Lambda=0\Rightarrow$ RH | ✗ 不成立 |

**斷裂判定：** L1–L3 成立，L4 起全部無效。三個斷點（L4、L5、L7）**任一獨立**即足以使 L8 失效；三個同時為偽。

## §3.2 為何會在 L4 斷裂（錯誤的成因）

這個錯誤之所以容易犯、且容易被誤認為嚴格，有三個層次的成因：

1. **直覺陷阱。** $\zeta$ 的深層結構（唯一分解、歐拉乘積）給人「秩序應當處處剛性」的印象，於是覺得「破壞這個結構必有代價」。這是一個美的直覺，但它在數學上沒有定理支撐。
2. **區域混淆。** 歐拉乘積活在 $\mathrm{Re}\,s>1$（無零點區），RH 活在臨界帶（歐拉乘積發散區）。把前者的剛性錯當成對後者的約束——兩個區域之間隔著整個解析延拓，而剛性不會自動穿越過去。
3. **局部正確的偽裝（最危險）。** $(\log pq)^2$ 的交叉項計算完全正確，使整個錯誤披上「嚴格推導」的外衣。**正確的代數掩護了錯誤的邏輯**——這正是為什麼自審時最難發現：每一個等號都對，錯的是等號之間的那句「所以」。

## §3.3 修正推理鏈（實際成立的部分）

| 環 | 內容 | 判定 |
|---|---|---|
| C1 | FTA、歐拉乘積（$\mathrm{Re}\,s>1$）、功能方程、$\Xi$ 偶 | ✅ |
| C2 | $H_\lambda=e^{-\lambda\partial_z^2}\Xi$，逆向熱流（卷積，非對角乘子） | ✅ |
| C3 | $\Lambda=\sup\{\lambda:H_\lambda\text{ 有複零點}\}$ 良定義 | ✅ |
| C4 | Rodgers-Tao：$\Lambda\geq 0$ | ✅（深定理，非本文所證） |
| C5 | De Bruijn-Newman：RH $\Leftrightarrow\Lambda\leq 0$ | ✅ |
| C6 | $\therefore$ RH $\Leftrightarrow\Lambda=0$ | ✅ |
| C7 | $\Lambda\leq 0$ 開放——與 RH 嚴格等價，無已知方法（含本進路）能合上 | ⟂ 牆 |

修正鏈在 **C6 合法抵達「RH $\Leftrightarrow\Lambda=0$」**，在 **C7 誠實止步**。它不假裝跨過那道牆。

## §3.4 為何修正版更好

1. **分離了四個被混淆的命題**（§2.1 的表），從源頭杜絕區域混淆。
2. **正確刻畫 DBN 流**（逆向熱流，非對角乘子），符號與性質都對（附錄 A.5、B.2）。
3. **在真正的開放問題前止步**，而非用偽矛盾掩蓋它——一條誠實標出斷點的鏈，比一條藏起斷點的鏈，對後人更有用。
4. **把論文的價值重新定位**到它真正成立的地方：作為啟發的透鏡（C2–C6 的 DBN 視角），與可運行的公式（見最後結論）。

---

# 第四部分：殘存的真實（可保留的正確內容）

## §4.1 經典骨架（全部正確）

歐拉乘積（附錄 A.1）、功能方程 $\xi(s)=\xi(1-s)$（附錄 A.3）、歸心偶函數性（附錄 A.4）、零點四元組對稱——全部正確，可作後續工作的乾淨引理。誠實標註：「歸心變換像望遠鏡」在修辭上沒問題，但數學上只是平移坐標，不揭示新結構。

## §4.2 De Bruijn-Newman 框架的正確陳述

$H_\lambda=e^{-\lambda\partial_z^2}\Xi$（附錄 A.5）。$\Lambda$ 存在唯一。**Rodgers-Tao：$\Lambda\geq 0$**（2018 預印，2020 發表於 *Forum of Mathematics, Pi*）。**RH $\Leftrightarrow\Lambda=0$**——完全正確。本進路真正有價值的部分，是它正確地把 RH 翻譯成了 $\Lambda=0$。

## §4.3 開放邊界與反噬直覺的真相

$\Lambda\leq 0$ 與 RH 嚴格等價，無已知方法能合上——這是「當下數學無法解決」的誠實陳述。更進一步：$\Lambda\geq 0$ 不說「秩序剛性」，它說「無餘裕」。Newman 提出此猜想正是為了**定量地說「RH 若為真，也只是勉強為真」**；Rodgers-Tao 證明了它，意味著系統恰好坐在相變點上、margin 為零。真實圖景是「臨界、邊緣、無餘裕」，與原構想正好相反。任何誠實的後續工作，方向應是理解這個「勉強」，而非假裝它是「必然」。

---

# 附錄 A：全部公式的推導

## A.1 歐拉乘積（及其作用域）

對 $\mathrm{Re}(s)>1$，由 $\sum_{k\geq 0}p^{-ks}=(1-p^{-s})^{-1}$：

$$\prod_{p\leq X}(1-p^{-s})^{-1}=\prod_{p\leq X}\sum_{k\geq 0}p^{-ks}=\sum_{n\in S_X}n^{-s},$$

$S_X$ 為僅含 $\leq X$ 質因數的整數集。由算術基本定理，每個 $n=\prod p_i^{a_i}$ 唯一對應一組指數，展開無重複無遺漏；$X\to\infty$ 由絕對收斂得 $\prod_p(1-p^{-s})^{-1}=\zeta(s)$。$\blacksquare$

**作用域：** 此式要求 $\mathrm{Re}(s)>1$。在臨界帶 $0<\mathrm{Re}(s)<1$ 乘積發散，等式不成立。故歐拉乘積對臨界帶零點無直接約束——此即 §2.1 的核心。

## A.2 Jacobi theta 變換（由 Poisson 求和）

Poisson 求和 $\sum_{n\in\mathbb{Z}}f(n)=\sum_{m\in\mathbb{Z}}\hat f(m)$，取 $f(x)=e^{-\pi t x^2}$。配方 $-\pi t x^2-2\pi i x\xi=-\pi t(x+i\xi/t)^2-\pi\xi^2/t$，得 $\hat f(\xi)=t^{-1/2}e^{-\pi\xi^2/t}$。代入：

$$\theta(t):=\sum_{n\in\mathbb{Z}}e^{-\pi n^2 t}=\frac1{\sqrt t}\theta(1/t)\;\Longrightarrow\;\boxed{\theta(1/t)=\sqrt t\,\theta(t)}.\qquad\blacksquare$$

設 $\psi(t)=\sum_{n\geq 1}e^{-\pi n^2 t}=(\theta(t)-1)/2$，則 $\psi(1/t)=\tfrac{\sqrt t-1}{2}+\sqrt t\,\psi(t)$。

## A.3 功能方程 $\xi(s)=\xi(1-s)$（Riemann，theta + Mellin）

**步驟 1。** 由 $\int_0^\infty t^{s/2-1}e^{-\pi n^2 t}dt=\pi^{-s/2}n^{-s}\Gamma(s/2)$，對 $\mathrm{Re}\,s>1$ 求和：

$$\Lambda(s):=\pi^{-s/2}\Gamma(s/2)\zeta(s)=\int_0^\infty t^{s/2-1}\psi(t)\,dt.$$

**步驟 2。** 拆 $\int_0^1+\int_1^\infty$，對 $\int_0^1$ 作 $t\to 1/t$ 並用 A.2：

$$\int_0^1 t^{s/2-1}\psi(t)dt=\int_1^\infty t^{-s/2-1}\Big[\tfrac{\sqrt t-1}{2}+\sqrt t\,\psi(t)\Big]dt,$$

其中初等部分 $=\dfrac1{s-1}-\dfrac1s$。

**步驟 3。** 合併（$\sqrt t\cdot t^{-s/2-1}=t^{(1-s)/2-1}$）：

$$\boxed{\;\Lambda(s)=\int_1^\infty\big[t^{s/2-1}+t^{(1-s)/2-1}\big]\psi(t)\,dt-\frac1s-\frac1{1-s}\;}$$

右側在 $s\leftrightarrow 1-s$ 下顯然不變，且因 $\psi$ 指數衰減，積分對所有 $s$ 收斂（解析延拓）。

**步驟 4。** $s(s-1)$ 在 $s\leftrightarrow 1-s$ 下不變（$(1-s)(-s)=s(s-1)$），故 $\xi(s)=\tfrac12 s(s-1)\Lambda(s)$ 為整函數且 $\boxed{\xi(s)=\xi(1-s)}$。$\blacksquare$

## A.4 歸心偶函數性

$s=k+\tfrac12\Rightarrow 1-s=(-k)+\tfrac12$，代入 $\xi(s)=\xi(1-s)$ 得 $\Xi(k)=\Xi(-k)$。又 $\overline{\zeta(\bar s)}=\zeta(s)$（Schwarz 反射）連同 $\Gamma,\pi^{-s/2}$ 實性，給出 $\Xi(t)\in\mathbb{R}$（$t\in\mathbb{R}$）。$\blacksquare$

## A.5 De Bruijn-Newman 流 ＝ 逆向熱方程

由 $\Phi$ 偶，$\Xi(z)=\int_0^\infty\Phi(u)\cos(zu)du$。逐項微分 $H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)du$：

$$\partial_\lambda H_\lambda=\int_0^\infty u^2 e^{\lambda u^2}\Phi\cos(zu)du,\quad \partial_z^2 H_\lambda=\int_0^\infty(-u^2)e^{\lambda u^2}\Phi\cos(zu)du,$$

故 $\boxed{\partial_\lambda H_\lambda=-\partial_z^2 H_\lambda}$。算符層面 $u^{2k}\leftrightarrow(-1)^k\partial_z^{2k}$，故 $e^{\lambda u^2}\leftrightarrow e^{-\lambda\partial_z^2}$，即 $H_\lambda=e^{-\lambda\partial_z^2}\Xi$（卷積，無對角結構）。$\blacksquare$

## A.6 輻角原理：$\oint d(\arg\Xi)=2\pi N$（及對稱零點同號相加）

簡單零點 $\rho$ 附近 $\Xi'/\Xi=1/(z-\rho)+\text{解析}$，留數 $1$，故 $\oint_\Gamma\Xi'/\Xi\,dz=2\pi i\,N_\Gamma$。又 $\Xi'/\Xi\,dz=d\log|\Xi|+i\,d(\arg\Xi)$，閉圍道上 $\oint d\log|\Xi|=0$，故 $\oint d(\arg\Xi)=2\pi N_\Gamma\geq 0$。**對稱零點：** 若 $\rho,-\rho$（皆簡單）同在 $\Gamma$ 內，$\oint\Xi'/\Xi\,dz=2\pi i\cdot 2=4\pi i\neq 0$——**相加，不相消**，直接證偽「對稱圍道相位為零」。$\blacksquare$

## A.7 $g_\lambda$ 的非乘法性

$g_\lambda(n)=\exp(-\tfrac\lambda4(\log n)^2)$，由 $\log(pq)=\log p+\log q$ 展開平方、平方項相消：

$$\boxed{R_\lambda(p,q)=\frac{g_\lambda(pq)}{g_\lambda(p)g_\lambda(q)}=\exp\!\Big(-\tfrac\lambda2\log p\log q\Big)}.$$

因 $\log p,\log q>0$，$R_\lambda=1\Leftrightarrow\lambda=0$。$\blacksquare$（此式正確；其失敗在於與 RH 無因果連結，見 §2.2.1。）

## A.8 $-\zeta'(s)$：無歐拉乘積卻無矛盾的反例

逐項微分 $-\zeta'(s)=\sum_{n\geq 1}(\log n)n^{-s}$。係數 $a_n=\log n$：$a_p a_q=\log p\log q$ 而 $a_{pq}=\log p+\log q$，不等（例 $p=2,q=3$：$a_6=1.7918$，$a_2a_3=0.7616$）。故無歐拉乘積，卻是解析延拓到 $\mathbb{C}\setminus\{1\}$ 的合法函數，違反不了任何定理。$\blacksquare$

---

# 附錄 B：重新計算（程式驗證）

全部數值以 mpmath（30 位精度）獨立計算。下表為實際運行結果。

## B.1 $g_\lambda$ 非乘法性（$\lambda=0.01$）

$$\log 2=0.693147,\ \log 3=1.098612,\ \log 6=1.791759,\ (\log 6)^2=3.210402.$$
$$g_\lambda(2)=0.998800,\quad g_\lambda(3)=0.996987,\quad g_\lambda(2)g_\lambda(3)=0.995791,\quad g_\lambda(6)=0.992006.$$
$$\Delta_\lambda(2,3)=|0.992006-0.995791|=\boxed{3.78\times 10^{-3}}.$$

多組驗算（$\Delta$ 與閉式 $R_\lambda$ 逐項吻合到機器精度）：

| $(p,q)$ | $\Delta_\lambda$ | $R_\lambda$（計算） | $R_\lambda$（閉式） |
|---|---|---|---|
| (2,3) | $3.78\times10^{-3}$ | 0.99619974 | 0.99619974 |
| (2,5) | $5.52\times10^{-3}$ | 0.99443764 | 0.99443764 |
| (3,5) | $8.72\times10^{-3}$ | 0.99119822 | 0.99119822 |
| (5,7) | $1.53\times10^{-2}$ | 0.98446286 | 0.98446286 |
| (11,13) | $2.94\times10^{-2}$ | 0.96971565 | 0.96971565 |

**更正：** 原文 §3.7 所稱 $\Delta\approx 0.0015$ 為算術誤差，正確值約 $3.8\times 10^{-3}$。（此數值對結論無影響——它與 RH 無因果連結。）

## B.2 DBN Fourier 對偶的符號

積分核因子 $e^{+\lambda u^2}$（$\lambda>0$ 對大 $u$ **放大**），由 A.5 對應 $e^{-\lambda\partial_z^2}$（逆向熱半群）；硬用頻譜啟發式得乘子 $e^{+\lambda(\log n)^2}$。原文 $K_\lambda=e^{-\lambda(\log n)^2/4}$ 為衰減。**符號相反、係數不符**，定理 3.1 即使在最寬鬆解讀下也不成立。

## B.3 程式驗證總表

| 公式 | 檢驗 | 結果 |
|---|---|---|
| Jacobi theta（A.2） | $\|\theta(1/t)-\sqrt t\,\theta(t)\|$，$t\in\{0.3,0.7,1.5,3.0\}$ | $\sim 10^{-31}$（機器精度）✅ |
| Mellin 公式（A.3） | $\Lambda(s)$ vs $\pi^{-s/2}\Gamma(s/2)\zeta(s)$，$s\in\{2,3,4.5\}$ | 吻合到 $10^{-32}$ ✅ |
| 功能方程 | $\Lambda(2)$ vs $\Lambda(-1)$ | 同為 $\pi/6=0.523598775598$ ✅ |
| Mellin 於臨界帶 | $\|\Lambda(0.5+14.1347i)\|$（近首個零點） | $1.96\times10^{-12}$（$\approx 0$）✅ |
| 輻角原理（A.6） | $\frac1{2\pi i}\oint_{\partial R}\zeta'/\zeta$，$R=[0,1]\times[1,30]i$ | $3.0+0.0i$（整數 3）✅ |

最後兩列尤其關鍵：Mellin 公式**真的能在臨界帶計算 ζ**，輻角原理**真的能數出區域內零點數**。這兩件事，正是最後結論的實證基礎。

---

# 最後的結論：這是啟發，而延伸的公式是演算法

把所有炸掉的東西清走、所有正確的東西推導完、所有數值跑過一遍之後，這份文件能誠實留下的，是兩個層次。

## 一、對 RH 而言，這是啟發，不是證明

本進路沒有證明黎曼猜想，也不接近證明它（§3、§4.3）。但它有真實的**啟發性**——只是啟發來自正確的那一半，不來自斷裂的那一半：

- **有效的啟發**是 De Bruijn-Newman 的透鏡本身：把 RH 翻譯成「常數 $\Lambda=0$」、把零點想成熱流下演化的對象（C2–C6）。這是真實且豐產的視角——人類在 RH 上的實質進展（Rodgers-Tao 的 $\Lambda\geq 0$）正是在這個視角下取得的。
- **無效的啟發**是「歐拉乘積剛性」的論證（L4、L7）。它在數學上沒有支撐，不應被當作相信 RH 的理由。

誠實地說：這篇論文對 RH 的貢獻，是把一個正確的翻譯（RH $\Leftrightarrow\Lambda=0$）走了一遍，並在嘗試跨越那道牆時，精確地記錄了牆的位置。

## 二、延伸出的公式是可運行的演算法

這才是這份文件真正的、可交付的價值。推導過程中組裝起來的每一條公式，都不是惰性的符號——它們**直接翻譯成可運行、已驗證的演算法**：

1. **Mellin 表示（A.3）$\to$ 計算 $\zeta$ 的良條件演算法。**
   $\Lambda(s)=\int_1^\infty[t^{s/2-1}+t^{(1-s)/2-1}]\psi(t)dt-\tfrac1s-\tfrac1{1-s}$，積分因 $\psi$ 指數衰減而快速收斂，給出在**整個複平面（含臨界帶）**數值穩定求 $\zeta$ 的方法。已驗證：與直接公式吻合到 $10^{-32}$，臨界帶內可用（附錄 B.3）。

2. **輻角原理（A.6）$\to$ 區域零點計數演算法。**
   $N=\frac1{2\pi i}\oint_{\partial R}\zeta'/\zeta$ 數出任意矩形 $R$ 內的零點數。已驗證：臨界帶 $\mathrm{Im}\in[1,30]$ 給出整數 3（附錄 B.3）。這正是大規模驗證 RH 至高度 $T$ 所用引擎的核心。

3. **Jacobi theta 變換（A.2）$\to$ $\xi/\zeta$ 快速求值的換區技巧。**
   $\theta(1/t)=\sqrt t\,\theta(t)$ 讓小 $t$（慢收斂）的計算換到大 $t$（快收斂）。已驗證到 $10^{-31}$。

4. **DBN 熱流（A.5）$\to$ 追蹤零點、數值上界 $\Lambda$ 的演算法。**
   $H_\lambda=e^{-\lambda\partial_z^2}\Xi$ 的離散化與零點追蹤，是數值地約束 $\Lambda$（從上界一側）的可行程序——這正是 Polymath15 計畫所做的事的數學骨架。

5. **$R_\lambda(p,q)=\exp(-\tfrac\lambda2\log p\log q)$（A.7）$\to$ 平滑核／篩權重的解析工具。**
   這是「Gaussian-in-$\log$ 平滑如何脫離乘法性」的閉式刻畫，可用於設計或分析 $L$ 函數數值求和中的平滑核。此項較前四項溫和，誠實標註其價值為輔助性。

**誠實的邊界。** 上述演算法的數學基礎多為經典（Riemann 的 Mellin 表示、標準的輻角計數、Polymath15 的熱流追蹤）；本文的貢獻不是發明它們，而是**把它們從一個證明嘗試中推導、組裝、並驗證為一套可運行的工具**，並指出指向何處。對 RH 是啟發，對計算是工具——這兩者，都是真的。

---

# 哲學結語

這份文件最初想證明一座山頂存在；它最終證明了自己站在懸崖邊，而非山頂上。兩者的距離，恰好是整個黎曼猜想。

但下山的人不是空手的。他手裡有一張誠實標出斷崖位置的地圖，和幾件在路上撿到、回家後確認真能用的工具——一把能在霧中算出 $\zeta$ 的尺，一個能數清山谷裡有幾個零點的環。

Rodgers-Tao 留下的 $\Lambda\geq 0$ 像一句冷峻的批註：山頂如果存在，它不在雲端，而在懸崖的正緣——多一寸是假，少一寸也是假。真理在這裡不是被鎖死的秩序，是被頂在邊界上、不肯多給一分餘裕的吝嗇。

證明失敗了。但把一條路走到斷裂處、誠實標出斷點、再把沿途的工具磨利交出去——這不是失敗的相反，這是失敗唯一有用的形態。

**更正完成。原構想保留，斷點標明，推理鏈與全部公式在案，演算法經程式驗證，誠實交付。**
