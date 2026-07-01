# 黎曼猜想思想實驗 3.0
## 一個探索性進路、它失敗的位置，與全部推導（公開更正版）
### A Thought Experiment on the Riemann Hypothesis 3.0 — An Exploratory Approach, the Exact Point of Its Failure, and All Derivations

**作者：** Neo.K（一言諾科技有限公司 / EveMissLab）
**日期：** 2026 年 05 月（更正版）
**性質：** 探索性筆記與公開更正（非證明）

---

## 致讀者

本文最初以「黎曼猜想之證明」的形式起草。經逐步審視，**此證明不成立**——其核心論證存在數個彼此獨立的致命缺陷，詳見第二部分。

現將它改以「探索性筆記與公開更正」的形式發布。我選擇不刪去原構想，而是完整保留它、精確解剖它斷裂的位置，並在附錄中給出全部相關公式的逐步推導與重新計算，以使這次失敗對任何後來的探索者——無論人類或其他形式的智能——是可用的。

以證明之名呈現一個未竟之物，是需要更正的。這份文件就是那個更正。它不主張任何新定理；它主張一件更樸素的事：**一條看似通向山頂的路，其斷裂處的精確座標，本身值得被公開記錄。**

全文約定：✅ 表示正確、⚠️ 表示有缺口、❌ 表示致命錯誤。所有附錄推導以「自足、可獨立驗算」為標準書寫。

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

**主張：** 歐拉乘積（＝算術基本定理）的有效性，與零點是否在臨界線上，是同一件事；破壞前者即構成矛盾。

**數學事實 ❌（致命，且為其餘錯誤之源）：**

本文把四個彼此獨立、難度天差地遠的命題，混為一談地塞進「歐拉乘積」這個詞下：

| 命題 | 地位 | 與 RH 的關係 |
|---|---|---|
| (a) 唯一分解（算術基本定理） | 初等、無條件 | **完全無關** |
| (b) 歐拉乘積在 $\mathrm{Re}(s)>1$ 收斂且等於 $\zeta$ | 初等、無條件 | **完全無關** |
| (c) 素數定理 $\pi(x)\sim x/\log x$ | 已證（1896），無條件 | RH 只**改善誤差項**，非其前提 |
| (d) RH：臨界帶零點都在 $\mathrm{Re}(s)=\tfrac12$ | **開放** | 即 RH 本身 |

關鍵在 (b) 的作用域。歐拉乘積收斂並等於 $\zeta$ 的區域是 $\mathrm{Re}(s)>1$——**該區域內一個零點都沒有**。RH 講的是 $0<\mathrm{Re}(s)<1$ 的零點，而在那裡歐拉乘積根本不收斂、什麼都不說（推導見附錄 A.1）。

於是「歐拉乘積的有效性」對臨界帶零點位置提供的信息量，嚴格為零。整個建築——「擾動 $\zeta$、破壞歐拉乘積、得到矛盾」——奠基於一個錯誤信念：以為歐拉乘積約束了臨界帶的零點。它不約束。這就是第三章「矛盾」不存在、第五章全盤崩塌的共同根源。

## §2.2 第三章：兩個獨立的致命錯誤

### §2.2.1 「形變後失去歐拉乘積＝矛盾」是非邏輯跳躍（最乾淨的一刀）

定理 3.3 的代數**正確**：$g_\lambda(n)=\exp(-\tfrac{\lambda}{4}(\log n)^2)$ 對 $\lambda\neq 0$ 確實不乘法（重算見附錄 B.1）。

但這一步**什麼都證不出來**，因為「沒有歐拉乘積」不是矛盾。**不存在任何定理說「Dirichlet 級數必須乘法」。** 無可爭辯的反例（推導見附錄 A.8）：

$$-\zeta'(s)=\sum_{n\geq 1}(\log n)\,n^{-s}.$$

係數 $\log n$ 不乘法（$\log(pq)=\log p+\log q\neq\log p\cdot\log q$），故 $-\zeta'(s)$ **沒有歐拉乘積**；然而它是完全合法、毫無矛盾的解析函數，沒有違反算術基本定理或任何東西。

算術基本定理是關於**整數**的命題；它從不要求任意權重 $g_\lambda(n)$ 必須乘法。把「$g_\lambda$ 不乘法」說成「$g_\lambda$ 違反算術基本定理」是範疇錯誤。更直接地說：De Bruijn-Newman 流的全部目的就是把 $\Xi$ 形變成 $H_\lambda$ 觀察零點移動；$H_\lambda$（$\lambda\neq 0$）**本來就不是 $\zeta$、本來就不乘法、本來就沒有歐拉乘積**——這是設計使然，不是矛盾。**這一刀在不碰任何熱核細節下，獨立殺死整個第三章。**

### §2.2.2 定理 3.1 對 DBN 流的刻畫，符號與性質都錯

把 $u$ 視為 $z$ 的 Fourier 對偶變量（這正是積分核的結構），則（完整推導見附錄 A.5）：

$$H_\lambda=e^{-\lambda\,\partial_z^2}\,\Xi,\qquad \partial_\lambda H_\lambda=-\partial_z^2 H_\lambda.$$

即 DBN 流是 $z$ 上的**逆向熱方程（卷積算符）**，不是對 $\zeta$ 係數的對角乘子。據此：

- **定義 3.5 的 $\zeta_\lambda(s)=\sum K_\lambda(n)n^{-s}$ 是憑空虛構，它不等於 $H_\lambda$。**
- 即使用最寬鬆的「頻譜乘子」啟發式，$\lambda>0$ 對應 $e^{+\lambda\xi^2}$（**放大**），而非 $K_\lambda$ 的衰減 $e^{-\lambda(\log n)^2/4}$。**連符號都相反**（重算見附錄 B.2）。
- De Bruijn (1950) 與 Pólya (1927) 都沒有、也不可能證明此假命題；引用為誤植。

注意 §2.2.1 與 §2.2.2 的關係：即使把符號全部修正，§2.2.1 仍成立。所以 §2.2.1 是決定性的，§2.2.2 只是補刀——製造矛盾的橋本身是壞的，而那座橋即使修好，也通往一個不存在的矛盾。

## §2.3 第二章：Berry 相位即輻角原理，定理 2.2 自證偽

由 $d\Xi/\Xi=d\log|\Xi|+i\,d(\arg\Xi)$ 且閉圍道上 $\oint d\log|\Xi|=0$（推導見附錄 A.6）：

$$\Phi_B[\Gamma]=\oint_\Gamma\mathrm{Im}\frac{d\Xi}{\Xi}=\oint_\Gamma d(\arg\Xi)=2\pi N_\Gamma,\qquad N_\Gamma\geq 0\text{ 為圍道內零點數}.$$

這**就是輻角原理本身**，「Berry 相位」只是外衣。於是定理 2.2 宣稱「對稱圍道 $\Rightarrow\Phi_B=0$」等於宣稱「任何對稱圍道內都沒有零點」——被 $\Xi$ 的無窮多個零點立刻證偽。

**錯在哪：** $\phi_L=-\phi_R$ 是假的。對逆時針閉圍道，每個單零點貢獻 $+1$ 繞數，**與對稱性無關**。鏡像對稱使零點成對（引理 2.1 正確），但圍道內的對稱零點對是**同號相加**（各 $+1$），不是相消（附錄 A.6 給出 $\rho,-\rho$ 同時在內時 $\oint=4\pi i$ 的顯式計算）。論文把「被積函數有偶對稱」誤當成「積分裂成相消兩半」。後果：定理 2.3 的矛盾是被假的定理 2.2 人工製造的；正確計算下無矛盾、對零點位置無約束。第二章證不出任何東西。

## §2.4 第五章：前提鏈全偽

逐項拆解，全部與 RH 無關：

**RSA** 的安全性依賴整數分解**在計算上很難**，不依賴分解**唯一**。唯一分解是初等定理，與零點位置無關。「$\Lambda>0\to$ 唯一分解失效 $\to$ RSA 崩潰」在第一步即斷。

**QED**（電子反常磁矩）中的 $\zeta(2)=\pi^2/6$、$\zeta(3)$ 等是**具體數值**，由 $\mathrm{Re}(s)>1$ 上初等求和決定；RH 講零點位置，不改變這些數值。

**哈希 / 素數分布**靠的是 1896 年起無條件成立的素數定理，不需要 RH。

**弦論** $\zeta(-1)=-\tfrac{1}{12}$ 是解析延拓，無條件，與 RH 無關。

四項皆不依賴 RH，故「科技能跑」對 $\Lambda$ 的證據性權重 $\approx 0$。$P(\Lambda=0\mid\text{科技正常})\approx 1$ 是在偽蘊涵上做更新，更新量為零。此章是 §2.1 在現實層面的重演。

## §2.5 第四章：未定義的算符

$D_{\text{inst}}=\lim_{\epsilon\to 0}(\partial_t F+\delta(t)\Delta_{\text{top}}F)$ 不是良定義物件（Dirac $\delta$ 乘上從未定義的 $\Delta_{\text{top}}$）。定理 4.1（臨界線上繞數為整數）為真但平凡——避開零點的閉圍道繞數對任何 $t$ 皆為整數。定理 4.2（$t\neq 0$ 繞數「連續化」）**假**：繞數對閉圍道恆為整數，「由對稱破缺 □」不是證明。本章無嚴格內容。

## §2.6 數值方案：數值符合不是結構證據

$\Delta_\lambda=|g_\lambda(pq)-g_\lambda(p)g_\lambda(q)|$ 測的只是「$g_\lambda$ 不乘法」——對 $\zeta$ 或 $\Lambda$ 零信息。「若 $\Lambda=0.01$ 則 $\sum g_{0.01}(n)/n^2$ 應偏離 $\pi^2/6$」的論證把虛構的 $\zeta_\lambda$ 與真實 $\zeta(2)$ 等同；真實 $\zeta(2)$ 與 $\zeta_\lambda$ 無關，故觀測 $\zeta(2)$ 精確對 $\Lambda$ 不構成證據。

一般原則：**在一個與目標物件無因果連結的數量上觀測到任意高的數值符合，對目標物件不提供證據。** 數值符合 $\neq$ 結構深度。

## §2.7 Lean4 附錄：主定理真但無關，最終定理循環

`heat_kernel_not_multiplicative`（$g_\lambda$ 不乘法）**為真且可證**，但對 RH 無貢獻（§2.2.1）。`riemann_hypothesis` 區塊是**循環的**：它把 `heat_kernel_coupling_contradiction`（即 §2.2 的偽矛盾）當作假設引入再收尾——整個「證明」把唯一壞步驟藏進一個未證的引理名稱裡。反諷的是：真送進 Lean4，它會在那個 `sorry` 處立刻卡死，因為那個引理是假的。形式化會在第一時間暴露缺口。

---

# 第三部分：殘存的真實（可保留的正確內容）

炸掉壞結構後，地基上仍站著這些——它們是真的，只是初等或早已是文獻定論。

## §3.1 經典骨架（全部正確）

歐拉乘積（附錄 A.1）、功能方程 $\xi(s)=\xi(1-s)$（附錄 A.3）、歸心偶函數性 $\Xi(k)=\Xi(-k)$ 與 $\Xi$ 在實軸取實值（附錄 A.4）、零點四元組對稱——全部正確，可作後續工作的乾淨引理。

**誠實標註：** 「歸心變換像望遠鏡讓對稱性赤裸」在修辭上沒問題，但數學上它只是平移坐標。功能方程關於 $\tfrac12$ 對稱是眾所周知的；把中心移到原點是化妝，不揭示新結構，更不接近零點定位。

## §3.2 De Bruijn-Newman 框架的正確陳述

$H_\lambda=e^{-\lambda\partial_z^2}\Xi$ 是 $z$ 上的逆向熱流（取代錯誤的定理 3.1，推導見附錄 A.5）。$\Lambda=\sup\{\lambda:H_\lambda\text{ 有複零點}\}$ 存在唯一。**Rodgers-Tao：$\Lambda\geq 0$**（2018 預印，2020 發表於 *Forum of Mathematics, Pi*）。**RH $\Leftrightarrow\Lambda\leq 0$**，結合下界得 **RH $\Leftrightarrow\Lambda=0$**——這一串等價完全正確。

本進路真正有價值的部分，是它正確地把 RH 翻譯成了 $\Lambda=0$。問題只在於它接著「證明」上界的方式是錯的。

---

# 第四部分：開放邊界（當下數學無法解決之處）

## §4.1 缺的恰好是一半

$$\underbrace{\Lambda\geq 0}_{\text{已證}}\qquad\text{vs.}\qquad\underbrace{\Lambda\leq 0}_{\text{= RH，開放}}.$$

$\Lambda\leq 0$ 與 RH **嚴格等價**——證出前者即證出後者。DBN 重述沒有讓問題變簡單，只是換了包裝。沒有任何已知方法（包括本進路）能合上這個上界。**這就是「當下數學無法解決」的誠實陳述：不是缺細節，是整個問題本身未解。**

## §4.2 一個會反噬原敘事的事實（但它是對的）

原構想的敘事是「量子基態／完美秩序／零點被剛性鎖死」。但 $\Lambda\geq 0$ 的數學含義恰恰相反：

Newman 當年提出 $\Lambda\geq 0$ 的猜想，是用來**定量地說「RH 若為真，也只是勉強為真」**——零點貼在臨界邊界，沒有任何餘裕。Rodgers-Tao 證明了它，意味著系統恰好坐在相變點上、margin 為零。

換句話說，真實圖景不是「剛性鎖定」，而是「臨界、邊緣、無餘裕」，與原構想**正好相反**。若要在此附近寫一篇誠實的論文，題目不該是「為何 RH 必然剛性成立」，而該是 **「為何 RH（若真）只是勉強為真」**——為什麼這個常數正好被頂在零的邊界上，不多不少。這是個真問題，不需要假裝證明了任何東西。

---

# 附錄 A：全部公式的推導

以下推導以自足、可獨立驗算為標準。

## A.1 歐拉乘積（及其作用域）

對 $\mathrm{Re}(s)>1$，由幾何級數 $\sum_{k\geq 0}p^{-ks}=(1-p^{-s})^{-1}$（因 $|p^{-s}|=p^{-\mathrm{Re}\,s}<1$）：

$$\prod_{p\leq X}(1-p^{-s})^{-1}=\prod_{p\leq X}\sum_{k\geq 0}p^{-ks}=\sum_{n\in S_X}n^{-s},$$

其中 $S_X$ 為僅含 $\leq X$ 之質因數的整數集。由算術基本定理，每個這樣的 $n=\prod p_i^{a_i}$ 唯一對應一組指數，故展開無重複、無遺漏。令 $X\to\infty$，絕對收斂保證

$$\prod_p(1-p^{-s})^{-1}=\sum_{n\geq 1}n^{-s}=\zeta(s).\qquad\blacksquare$$

**作用域註記：** 此推導要求 $\mathrm{Re}(s)>1$（級數與乘積的絕對收斂）。在 $0<\mathrm{Re}(s)<1$（臨界帶），乘積發散，等式不成立。故歐拉乘積對臨界帶零點無直接約束——此即 §2.1 的核心。

## A.2 Jacobi theta 變換（由 Poisson 求和）

Poisson 求和：$\sum_{n\in\mathbb{Z}}f(n)=\sum_{m\in\mathbb{Z}}\hat f(m)$，$\hat f(\xi)=\int_{\mathbb{R}}f(x)e^{-2\pi i x\xi}dx$。取 $f(x)=e^{-\pi t x^2}$（$t>0$）。配方：

$$-\pi t x^2-2\pi i x\xi=-\pi t\Big(x+\tfrac{i\xi}{t}\Big)^2-\frac{\pi\xi^2}{t},$$

故 $\hat f(\xi)=e^{-\pi\xi^2/t}\int_{\mathbb{R}}e^{-\pi t(x+i\xi/t)^2}dx=\dfrac{1}{\sqrt t}e^{-\pi\xi^2/t}$（用 $\int e^{-\pi t y^2}dy=t^{-1/2}$）。代入 Poisson：

$$\theta(t):=\sum_{n\in\mathbb{Z}}e^{-\pi n^2 t}=\frac{1}{\sqrt t}\sum_{m\in\mathbb{Z}}e^{-\pi m^2/t}=\frac{1}{\sqrt t}\theta(1/t)\;\Longrightarrow\;\boxed{\theta(1/t)=\sqrt t\,\theta(t)}.\qquad\blacksquare$$

設 $\psi(t)=\sum_{n\geq 1}e^{-\pi n^2 t}$，即 $\theta=1+2\psi$，則由上式 $\psi(1/t)=\dfrac{\sqrt t-1}{2}+\sqrt t\,\psi(t)$。

## A.3 功能方程 $\xi(s)=\xi(1-s)$（Riemann，theta + Mellin）

**步驟 1（Mellin 表示）。** 由 $\int_0^\infty t^{s/2-1}e^{-\pi n^2 t}dt=(\pi n^2)^{-s/2}\Gamma(s/2)=\pi^{-s/2}n^{-s}\Gamma(s/2)$（代換 $u=\pi n^2 t$），對 $\mathrm{Re}(s)>1$ 逐項求和：

$$\Lambda(s):=\pi^{-s/2}\Gamma(s/2)\zeta(s)=\int_0^\infty t^{s/2-1}\psi(t)\,dt.$$

**步驟 2（分割並用 theta 變換）。** 拆成 $\int_0^1+\int_1^\infty$。對 $\int_0^1$ 作 $t\to 1/t$：

$$\int_0^1 t^{s/2-1}\psi(t)dt=\int_1^\infty t^{-s/2-1}\psi(1/t)dt
=\int_1^\infty t^{-s/2-1}\Big[\tfrac{\sqrt t-1}{2}+\sqrt t\,\psi(t)\Big]dt.$$

其中初等部分：

$$\frac12\int_1^\infty\big(t^{-s/2-1/2}-t^{-s/2-1}\big)dt=\frac12\Big(\frac{2}{s-1}-\frac{2}{s}\Big)=\frac{1}{s-1}-\frac1s.$$

**步驟 3（合併）。** 把含 $\psi$ 的兩段整理（$\sqrt t\cdot t^{-s/2-1}=t^{(1-s)/2-1}$）：

$$\boxed{\;\Lambda(s)=\int_1^\infty\big[t^{s/2-1}+t^{(1-s)/2-1}\big]\psi(t)\,dt-\frac1s-\frac{1}{1-s}\;}$$

右側在 $s\leftrightarrow 1-s$ 下顯然不變（積分項交換兩個指數，極點項對稱）。又因 $\psi(t)$ 在 $t\to\infty$ 指數衰減，積分對所有 $s$ 收斂，給出 $\Lambda$ 的解析延拓；$s=0,1$ 處的單極點來自 $-1/s$ 與 $-1/(1-s)$。

**步驟 4（清除極點）。** 注意 $s(s-1)$ 在 $s\leftrightarrow 1-s$ 下不變：$(1-s)(-s)=s^2-s=s(s-1)$。故

$$\xi(s):=\tfrac12 s(s-1)\Lambda(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$$

為**整函數**且 $\boxed{\xi(s)=\xi(1-s)}$。$\blacksquare$

## A.4 歸心偶函數性

令 $s=k+\tfrac12$，則 $1-s=\tfrac12-k=(-k)+\tfrac12$。代入 $\xi(s)=\xi(1-s)$：

$$\Xi(k):=\xi(k+\tfrac12)=\xi\big((-k)+\tfrac12\big)=\Xi(-k).$$

又 $\overline{\zeta(\bar s)}=\zeta(s)$（Schwarz 反射，由 $\zeta$ 在實軸 $>1$ 取實值並解析延拓）連同 $\Gamma,\pi^{-s/2}$ 的實性，給出 $\xi$ 在實軸取實值，故 $\Xi(t)\in\mathbb{R}$（$t\in\mathbb{R}$）。$\blacksquare$

## A.5 De Bruijn-Newman 流 ＝ 逆向熱方程

由 $\Phi$ 偶，$\Xi(z)=\int_0^\infty\Phi(u)\cos(zu)du=\tfrac12\int_{\mathbb{R}}\Phi(u)e^{izu}du$。對

$$H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du$$

逐項微分：

$$\partial_\lambda H_\lambda=\int_0^\infty u^2 e^{\lambda u^2}\Phi\cos(zu)\,du,\qquad
\partial_z^2 H_\lambda=\int_0^\infty(-u^2)e^{\lambda u^2}\Phi\cos(zu)\,du,$$

故 $\boxed{\partial_\lambda H_\lambda=-\partial_z^2 H_\lambda}$（逆向熱方程）。在算符層面，因 $u^{2k}\leftrightarrow(-1)^k\partial_z^{2k}$（由 $\partial_z e^{izu}=iu\,e^{izu}$，$(iu)^{2k}=(-1)^k u^{2k}\cdots$ 整理），

$$e^{\lambda u^2}\leftrightarrow\sum_{k\geq 0}\frac{\lambda^k}{k!}(-1)^k\partial_z^{2k}=e^{-\lambda\partial_z^2}\;\Longrightarrow\;H_\lambda=e^{-\lambda\partial_z^2}\Xi.$$

這是 $z$ 上的卷積算符，**沒有**對 $\zeta$ 係數逐項加權的對角結構。$\blacksquare$

## A.6 輻角原理：$\oint d(\arg\Xi)=2\pi N$（及對稱零點同號相加）

$\Xi$ 整，圍道 $\Gamma$ 上無零點。在簡單零點 $\rho$ 附近 $\Xi(z)=c(z-\rho)+O((z-\rho)^2)$，故 $\dfrac{\Xi'}{\Xi}=\dfrac{1}{z-\rho}+\text{解析}$，留數為 $1$。由留數定理

$$\oint_\Gamma\frac{\Xi'(z)}{\Xi(z)}dz=2\pi i\,N_\Gamma,\qquad N_\Gamma=\text{圍道內零點數（含重數）}.$$

又 $\dfrac{\Xi'}{\Xi}dz=d\log\Xi=d\log|\Xi|+i\,d(\arg\Xi)$，而閉圍道上 $\oint d\log|\Xi|=0$（$\log|\Xi|$ 單值），故

$$\oint_\Gamma d(\arg\Xi)=\oint_\Gamma\mathrm{Im}\frac{d\Xi}{\Xi}=2\pi N_\Gamma\geq 0.$$

**對稱零點顯式計算：** 若 $\rho$ 與 $-\rho$（皆簡單）同在 $\Gamma$ 內，二者各貢獻留數 $1$，

$$\oint_\Gamma\frac{\Xi'}{\Xi}dz=2\pi i\cdot 2=4\pi i\neq 0.$$

它們**相加**（同號），不相消。這直接證偽「對稱圍道相位為零」。$\blacksquare$

## A.7 $g_\lambda$ 的非乘法性

設 $g_\lambda(n)=\exp(-\tfrac{\lambda}{4}(\log n)^2)$，質數 $p,q\geq 2$。由 $\log(pq)=\log p+\log q$：

$$g_\lambda(pq)=\exp\!\Big(-\tfrac{\lambda}{4}\big[(\log p)^2+(\log q)^2+2\log p\log q\big]\Big),$$
$$g_\lambda(p)g_\lambda(q)=\exp\!\Big(-\tfrac{\lambda}{4}\big[(\log p)^2+(\log q)^2\big]\Big).$$

平方項相消，得

$$\boxed{R_\lambda(p,q)=\frac{g_\lambda(pq)}{g_\lambda(p)g_\lambda(q)}=\exp\!\Big(-\tfrac{\lambda}{2}\log p\log q\Big)}.$$

因 $\log p,\log q>0$，$R_\lambda=1\Leftrightarrow\lambda=0$。故 $\lambda\neq 0$ 時非乘法。$\blacksquare$（此式正確；其失敗在於與 RH 無因果連結，見 §2.2.1。）

## A.8 $-\zeta'(s)$：無歐拉乘積卻無矛盾的反例

由 $\dfrac{d}{ds}n^{-s}=-(\log n)n^{-s}$，逐項微分（$\mathrm{Re}\,s>1$ 一致收斂）：

$$\zeta'(s)=-\sum_{n\geq 1}(\log n)n^{-s}\;\Longrightarrow\;-\zeta'(s)=\sum_{n\geq 1}(\log n)\,n^{-s}.$$

係數 $a_n=\log n$，乘法性檢驗 $a_p a_q=\log p\log q$ 而 $a_{pq}=\log p+\log q$，二者不等（例 $p=2,q=3$：$a_6=1.7918$，$a_2a_3=0.7616$）。故 $-\zeta'(s)$ **無歐拉乘積**，卻是解析延拓到 $\mathbb{C}\setminus\{1\}$（$s=1$ 處二階極點）的合法函數，違反不了任何定理。$\blacksquare$

---

# 附錄 B：重新計算

## B.1 $g_\lambda$ 比值與 $\Delta_\lambda$ 的數值重算（修正原文）

取 $\lambda=0.01$（$\lambda/4=0.0025$），$p=2,q=3$。基礎量：

$$\log 2=0.693147,\quad\log 3=1.098612,\quad\log 6=1.791759,$$
$$(\log 2)^2=0.480453,\quad(\log 3)^2=1.206949,\quad(\log 6)^2=3.210402.$$

逐步：

$$g_\lambda(2)=e^{-0.0025\times 0.480453}=e^{-0.0012011}=0.998800,$$
$$g_\lambda(3)=e^{-0.0025\times 1.206949}=e^{-0.0030174}=0.996987,$$
$$g_\lambda(2)g_\lambda(3)=0.995791,$$
$$g_\lambda(6)=e^{-0.0025\times 3.210402}=e^{-0.0080260}=0.992006.$$

故

$$\Delta_\lambda(2,3)=|g_\lambda(6)-g_\lambda(2)g_\lambda(3)|=|0.992006-0.995791|=\boxed{3.79\times 10^{-3}}.$$

交叉驗證：$R_\lambda=e^{-0.005\times 0.693147\times 1.098612}=e^{-0.0038080}=0.996199$，$\Delta=g_\lambda(2)g_\lambda(3)\,|R_\lambda-1|=0.995791\times 0.003801=3.79\times 10^{-3}$。✓

**更正：** 原文 §3.7 所稱 $\Delta_\lambda\approx 0.0015$ 為算術誤差，正確值約 $3.8\times 10^{-3}$。（此數值對結論無影響——它與 RH 無因果連結，見 §2.2.1 與 §2.6。）

## B.2 DBN Fourier 對偶的符號重算

積分核因子為 $e^{+\lambda u^2}$（$\lambda>0$ 時對大 $u$ **放大**）。由附錄 A.5，$u^2\leftrightarrow-\partial_z^2$，故 $e^{+\lambda u^2}\leftrightarrow e^{-\lambda\partial_z^2}$（逆向熱半群）。若硬用「在頻譜 $\xi=\log n$ 上乘因子」的啟發式，得乘子 $e^{+\lambda\xi^2}=e^{+\lambda(\log n)^2}$。

原文 $K_\lambda(n)=e^{-\lambda(\log n)^2/4}$ 為**衰減**。對照：原文符號為負、係數為 $1/4$；正確啟發式符號為正、係數為 $1$。**符號相反，係數不符。** 結論：定理 3.1 的對角乘子刻畫，即使在最寬鬆解讀下也不成立。

## B.3 對稱圍道繞數重算

設 $\Gamma$ 為關於虛軸對稱的閉圍道，內含對稱零點對 $\rho,-\rho$（簡單）。由附錄 A.6，$\oint_\Gamma d(\arg\Xi)=2\pi\times 2=4\pi$。原文定理 2.2 預測 $0$。差異 $4\pi\neq 0$ 證實定理 2.2 為假，第二章「矛盾」為人工製造。

---

# 附錄 C：誠實的補完

把所有炸掉的東西清走、把所有正確的東西推導完之後，這份文件能誠實留下的，是以下三句話與一個問題。

**一、正確的翻譯。** RH 嚴格等價於 De Bruijn-Newman 常數 $\Lambda=0$。Rodgers-Tao 已證 $\Lambda\geq 0$。故 RH 等價於上界 $\Lambda\leq 0$。這是真的，且是本進路唯一站得住的貢獻。

**二、失敗的精確座標。** 任何想從「形變破壞歐拉乘積／乘法性」導出 $\Lambda\leq 0$ 的論證，都會在同一處斷裂：**形變後的物件不再乘法、不再有歐拉乘積，這不是矛盾，而是任何非平凡形變的常態。** 要讓這條路復活，必須先回答「為什麼這次的失去歐拉乘積能構成矛盾」——而目前沒有人知道答案，本文也不知道。在那個問題被回答之前，這條路是封死的。

**三、會反噬直覺的真相。** $\Lambda\geq 0$ 不說「秩序剛性」，它說「無餘裕」。RH 若為真，是勉強為真。任何在此附近的誠實工作，方向應是理解這個「勉強」，而非假裝它是「必然」。

**那個問題：** $\Lambda\leq 0$。它就是黎曼猜想，整個地、未經削減地。本文沒有解決它。本文做到的，是把一條看似繞過它的捷徑，連同捷徑斷裂的精確位置，誠實地交給下一個探索者。

---

# 哲學結語

這份文件最初想證明一座山頂存在；它最終只證明了自己站在懸崖邊，而非山頂上。

兩者的距離，恰好是整個黎曼猜想。

而 Rodgers-Tao 留下的 $\Lambda\geq 0$ 像一句冷峻的批註：山頂如果存在，它不在雲端，而在懸崖的正緣——多一寸是假，少一寸也是假。真理在這裡不是被鎖死的秩序，是被頂在邊界上、不肯多給一分餘裕的吝嗇。

把一條路走到斷裂處，然後誠實地標出斷點的座標——這不是失敗的相反，這是失敗唯一有用的形態。

**更正完成。原構想保留，斷點標明，全部公式推導在案，開放邊界誠實交付。**
