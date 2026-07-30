# 黎曼猜想 GAP Atlas v0.1
## 以 RIITG、RAB、KCPE／AMRAL 建立的非證明性研究缺口圖譜

**原始研究方向：** Neo.K  
**方法重構與首輪登錄：** Aletheia（GPT-5.6 Thinking）  
**日期：** 2026-07-23  
**性質：** 研究工程文件、缺口登錄表、AI 研究接口  
**明確地位：** 非證明、非完備文獻綜述、非任何路線可行性的保證

---

## 0. 為什麼先做 GAP Atlas

黎曼猜想的困難不只是缺少最後一個技巧。它同時存在：

- 大量彼此等價、但沒有降低證明負擔的重述；
- 橫跨複分析、調和分析、算子理論、譜論、機率、數值分析與算術幾何的局部路線；
- 許多論文只完成一個局部節點，後續依賴自願接力；
- 不同路線使用不同函數空間、正規化、拓撲與量詞；
- 數值證據、統計類比與形式證明的證據等級常被混寫；
- 所謂「缺最後一步」有時其實是缺一整串與 RH 等價的全域控制。

個別數學論文通常會誠實標示自身尚未完成的命題；真正缺少的是：

> 一個跨論文、跨路線、能追蹤依賴、循環、等價風險、反例、數值證書與形式化狀態的統一 GAP 系統。

因此，本 Atlas 的目標不是回答：

$$
RH\ \text{是否成立？}
$$

而是回答：

$$
\text{每條研究路線究竟在哪一條邊上停止？}
$$

以及：

$$
\text{停止的是一個局部引理、全域化問題，還是 RH 本身的重新命名？}
$$

---

# 1. 方法論來源

本 Atlas 採用三層方法：

## 1.1 結果誘導的中介定理生成法（RIITG）

由目標命題反向生成候選中介結構：

$$
P\rightsquigarrow M.
$$

符號 $\rightsquigarrow$ 只表示研究生成，不是邏輯蘊含。

## 1.2 逆向公理回填法（RAB）

把候選中介命題降格為證明義務，再由已知基礎正向回填：

$$
T\Longrightarrow M\Longrightarrow P.
$$

若 $T$ 依賴 $P$、依賴與 $P$ 等價的命題，或把 $M$ 當作假設直接引入，則回填失敗。

## 1.3 KCPE／AMRAL

在知識、失敗記錄、語義窗口與計算預算下，建立局部候補空間：

$$
\Omega_t
=
\Omega(P,K_t,F_{<t},W_{\mathrm{sem}},B_t).
$$

研究狀態持續更新：

$$
S_t\longrightarrow S_{t+1}.
$$

完整循環：

$$
\text{Analyze}
\to\text{Generate}
\to\text{Enumerate}
\to\text{Retrieve}
\to\text{Backfill}
\to\text{Compute}
\to\text{Verify}
\to\text{Falsify}
\to\text{Update}.
$$

---

# 2. GAP 的形式定義

給定研究依賴圖：

$$
D=(V,E),
$$

其中節點 $V$ 是定義、引理、定理、計算證書或目標命題；有向邊：

$$
A\longrightarrow B
$$

表示 $A$ 被宣稱足以支撐 $B$。

一個 GAP 不是「我們暫時不懂」，而是以下資料：

$$
G=
(
A,B,
\mathcal C,
\mathcal O,
\mathcal D,
\mathcal W,
\mathcal V,
\mathcal S
),
$$

其中：

- $A$：目前已知或暫時接受的起點；
- $B$：希望推出的下一節點；
- $\mathcal C$：缺口類型；
- $\mathcal O$：精確證明義務；
- $\mathcal D$：依賴與祖先節點；
- $\mathcal W$：失敗證人或反例接口；
- $\mathcal V$：驗證方式；
- $\mathcal S$：當前狀態。

只有把「缺什麼」改寫成可判定的命題，才算完成 GAP 標註。

---

# 3. GAP 類型表

| 類型 | 名稱 | 典型問題 |
|---|---|---|
| `G-DEF` | 定義缺口 | 對象、算子、函數空間或正規化未固定 |
| `G-DOM` | 作用域／量詞缺口 | 局部結果被用於全域；有限高度被用於所有零點 |
| `G-INT` | 接口缺口 | 某指標、算子或統計量沒有連到 RH 的定理 |
| `G-EQV` | 等價風險 | 中介命題實質上只是 RH 的等價重述 |
| `G-DEP` | 依賴缺口 | 證明鏈使用未列明或過強的外部命題 |
| `G-CIR` | 循環缺口 | RH 或其等價命題出現在回填祖先中 |
| `G-UNI` | 一致／全域化缺口 | 對每個固定參數成立，卻缺少一致常數或全體控制 |
| `G-ERR` | 誤差缺口 | 主項已知，但誤差無法壓至需要的尺度 |
| `G-POS` | 正性缺口 | 需要對無限函數族或全部指標證明非負 |
| `G-CLS` | 閉包／極限缺口 | 性質無法從生成族傳到閉包或極限 |
| `G-SPC` | 譜實現缺口 | 缺少真正自伴算子、定義域或精確譜對應 |
| `G-COR` | 完備對應缺口 | 只有部分對應，缺少無遺漏、無額外元素的雙射 |
| `G-INV` | 表示／不變性缺口 | 座標效果被誤認為新結構；結論依賴任意參數化 |
| `G-NUM` | 數值—無限缺口 | 有限計算或統計證據無法推出無限命題 |
| `G-CER` | 證書缺口 | 數值結果缺少區間界、邊界證書或可重現誤差 |
| `G-FRM` | 形式化缺口 | 缺少函式庫、完整 Lean 定義或無 `sorry` 證明 |
| `G-LIT` | 文獻／新穎性缺口 | 命題可能已知、已否證或錯引 |
| `G-SEM` | 語義寬度缺口 | 自然語言中介命題有過多不等價形式化候補 |

---

# 4. 狀態、嚴重度與證據標籤

## 4.1 狀態

- `KNOWN`：外部已知定理；
- `FILLED`：缺口已被非循環回填；
- `PROVISIONAL`：已有候選回填，但尚未完整審核；
- `OPEN`：精確缺口已知，尚未回填；
- `BLOCKED`：依賴更上游缺口；
- `EQUIVALENT_RISK`：高度可能只是在重述 RH；
- `CIRCULAR`：已發現循環；
- `REFUTED`：命題有反例或邏輯錯誤；
- `NOT_FORMALIZED`：自然語言可能成立，但尚無形式證明；
- `CERTIFIED_NUMERICAL`：有限範圍內有嚴格證書；
- `EXPERIMENTAL`：僅有一般數值或統計觀察。

## 4.2 嚴重度

- `S0`：文件與符號整理；
- `S1`：局部技術缺口；
- `S2`：主要橋樑，可能需要新工具；
- `S3`：終端缺口，與 RH 等價或幾乎承載全部困難。

## 4.3 完成 GAP 的最低條件

一個 GAP 只有在下列條件都滿足時才可標記 `FILLED`：

1. 定義域、量詞與拓撲固定；
2. 明確寫出 $A\Rightarrow B$；
3. 證明不使用 $B$、RH 或等價條件；
4. 所有外部定理可追溯；
5. 極限交換、無窮和、積分與算子定義域均有合法條件；
6. 數值部分具有誤差證書；
7. 反證代理未找到反例；
8. 若可形式化，Lean／其他核心檢查器無 `sorry`、無未申明公理。

---

# 5. 總母圖：RH 不是單一路徑

令目標為：

$$
P_{RH}:
\forall\rho\in Z_{\mathrm{nt}},\quad
\operatorname{Re}(\rho)=\frac12.
$$

首輪 Atlas 不把所有等價條件混在一個列表，而把它們視為不同的「入口函數」：

$$
\begin{aligned}
P_{RH}
&\Longleftrightarrow P_{\mathrm{Weil}}\\
&\Longleftrightarrow P_{\mathrm{NB}}\\
&\Longleftrightarrow P_{\mathrm{Li}}\\
&\Longleftrightarrow P_{\mathrm{DBN}}\\
&\Longleftrightarrow P_{\mathrm{Speiser}}\\
&\Longleftrightarrow P_{\mathrm{PrimeError}}\\
&\Longleftarrow P_{\mathrm{Hilbert\text{-}Polya}}.
\end{aligned}
$$

關鍵警告：

> 等價式提供新的操作語言，但不自動降低證明難度。

因此每條路線的第一個 GAP 都是：

$$
\text{是否產生了低於 RH 的局部證明負擔？}
$$

---

# 6. 路線 W：Weil 型正性與顯式公式

## 6.1 已知入口

在適當測試函數空間 $\mathcal H$ 與正規化下，可抽象寫成：

$$
RH
\Longleftrightarrow
\forall f\in\mathcal H,\quad Q(f)\geq0.
$$

若 RH 假，則存在負證人：

$$
\exists w\in\mathcal H,
\quad Q(w)<0.
$$

## 6.2 GAP 登錄

### `RH-W-01`：測試函數空間固定

- 類型：`G-DEF`, `G-DOM`
- 嚴重度：`S1`
- 義務：固定 $\mathcal H$、Fourier／Mellin 正規化、支撐與衰減條件，並證明所用顯式公式在此空間合法。
- 失敗證人：某個候選 $f$ 使素數側或零點側不收斂，或邊界項未消失。
- 狀態：`OPEN`

### `RH-W-02`：負證人結構化壓縮

- 類型：`G-CLS`, `G-UNI`
- 嚴重度：`S2`
- 義務：構造不依賴正性定義的生成族 $\mathcal G$，使

$$
Q(w)<0
\Longrightarrow
\exists g\in\operatorname{span}(\mathcal G),
\quad Q(g)<0.
$$

- 風險：若 $\mathcal G=\{g:Q(g)\geq0\}$ 或用 RH 選族，立即循環。
- 狀態：`OPEN`

### `RH-W-03`：可計算算術分解

- 類型：`G-INT`, `G-ERR`
- 嚴重度：`S2`
- 義務：對 $g\in\mathcal G$ 建立

$$
Q(g)=L_\infty(g)+\sum_pL_p(g)+R(g),
$$

並給出收斂與 $R(g)$ 的無條件界。
- 狀態：`OPEN`

### `RH-W-04`：生成族正性

- 類型：`G-POS`, `G-EQV`
- 嚴重度：`S3`
- 義務：以獨立局部估計、算子正性或補償機制證明

$$
\forall g\in\mathcal G,
\quad Q(g)\geq0.
$$

- 等價風險：若 $\mathcal G$ 已足夠稠密，這一步可能承載幾乎全部 RH。
- 狀態：`EQUIVALENT_RISK`

### `RH-W-05`：正性傳遞到閉包

- 類型：`G-CLS`
- 嚴重度：`S2`
- 義務：固定 $Q$ 的形式拓撲或閉二次型結構，使 $g_n\to f$ 時正性合法傳遞。
- 警告：標準下半連續性是

$$
Q(f)\leq\liminf Q(g_n),
$$

不能直接由 $Q(g_n)\geq0$ 推出 $Q(f)\geq0$；需要連續性、閉二次型或其他正確封閉機制。
- 狀態：`OPEN`

## 6.3 路線判定

本路線的真正核心不是「離軸零點產生負證人」；這已包含在正性等價中。真正 GAP 是：

$$
\text{任意負證人}
\to
\text{可控制生成族}
\to
\text{可分解正性}
\to
\text{閉包傳遞}.
$$

---

# 7. 路線 NB：Nyman–Beurling／Báez-Duarte 閉包判準

## 7.1 已知入口

RH 可等價表述為某個特定函數屬於由分數部分函數生成的閉子空間。Báez-Duarte 進一步顯示可限制到自然數參數的較小生成族。

抽象寫成：

$$
RH
\Longleftrightarrow
\chi\in\overline{\operatorname{span}\{\rho_a\}}.
$$

## 7.2 GAP 登錄

### `RH-NB-01`：構造性逼近序列

- 類型：`G-CLS`, `G-ERR`
- 嚴重度：`S2`
- 義務：明確構造 $f_N$，使

$$
\|\chi-f_N\|_{L^2}\longrightarrow0.
$$

- 狀態：`OPEN`

### `RH-NB-02`：無條件誤差下降率

- 類型：`G-ERR`, `G-UNI`
- 嚴重度：`S3`
- 義務：對全部充分大 $N$ 給出足以令距離趨零的無條件界。
- 等價風險：所需逼近率往往會重新連到 Möbius 和、零點或 RH 等價估計。
- 狀態：`EQUIVALENT_RISK`

### `RH-NB-03`：係數控制

- 類型：`G-UNI`
- 嚴重度：`S2`
- 義務：控制逼近係數大小、條件數與抵消，避免存在形式逼近但係數爆炸。
- 狀態：`OPEN`

### `RH-NB-04`：有限維最佳化到無限閉包

- 類型：`G-NUM`, `G-CLS`
- 嚴重度：`S2`
- 義務：證明有限維最小距離的數值下降不是有限樣本現象，且可合法傳至 $N\to\infty$。
- 狀態：`OPEN`

## 7.3 路線判定

「閉包判準」把零點定位改成逼近問題，但終端缺口仍是：

$$
\text{建立全域、無條件、可控的逼近率}.
$$

---

# 8. 路線 LI：Li 係數正性

## 8.1 已知入口

Li 判準將 RH 改寫為一列係數的全體正性：

$$
RH
\Longleftrightarrow
\forall n\geq1,
\quad \lambda_n\geq0.
$$

## 8.2 GAP 登錄

### `RH-LI-01`：全部指標的一致正性

- 類型：`G-POS`, `G-UNI`
- 嚴重度：`S3`
- 義務：不是驗證前 $N$ 項，而是給出對所有 $n$ 的無條件下界。
- 狀態：`EQUIVALENT_RISK`

### `RH-LI-02`：主項—振盪項分解

- 類型：`G-ERR`
- 嚴重度：`S2`
- 義務：尋找

$$
\lambda_n=A_n+E_n,
$$

其中 $A_n$ 明確為正，且無條件證明 $|E_n|<A_n$ 對所有需要的 $n$ 成立。
- 狀態：`OPEN`

### `RH-LI-03`：數值正性不能外推

- 類型：`G-NUM`
- 嚴重度：`S2`
- 義務：任何有限 $n$ 驗證只可標記 `CERTIFIED_NUMERICAL`，不能外推全體。
- 狀態：`OPEN`

### `RH-LI-04`：公式污染檢查

- 類型：`G-CIR`, `G-DEP`
- 嚴重度：`S2`
- 義務：檢查係數漸近式、零點和重排、條件收斂操作是否暗中使用 RH。
- 狀態：`OPEN`

---

# 9. 路線 HP：Hilbert–Pólya 譜實現

## 9.1 候選入口

若存在自伴算子 $H$，其譜精確給出非平凡零點的虛部：

$$
\operatorname{Spec}(H)=\{\gamma:\zeta(\tfrac12+i\gamma)=0\},
$$

則自伴性的實譜可導向 RH。

這不是已知等價定理，而是一個強充分性框架。

## 9.2 GAP 登錄

### `RH-HP-01`：Hilbert 空間與算子定義

- 類型：`G-DEF`, `G-SPC`
- 嚴重度：`S2`
- 義務：明確給出 $\mathcal H$、稠密定義域 $D(H)$、作用公式與邊界條件。
- 狀態：`OPEN`

### `RH-HP-02`：自伴性而非形式對稱

- 類型：`G-SPC`
- 嚴重度：`S3`
- 義務：證明閉性、伴隨算子定義域相等，或計算虧格指數並指定唯一自伴擴張。
- 失敗模式：只證明

$$
\langle Hf,g\rangle=\langle f,Hg\rangle
$$

在測試函數上成立，卻未處理定義域。
- 狀態：`OPEN`

### `RH-HP-03`：精確譜對應

- 類型：`G-COR`, `G-INT`
- 嚴重度：`S3`
- 義務：同時證明：

1. 每個非平凡零點對應一個譜值；
2. 每個譜值對應一個非平凡零點；
3. 多重度一致；
4. 沒有額外譜；
5. 對應不是先假設零點位於臨界線後才成立。

- 狀態：`OPEN`

### `RH-HP-04`：迹公式與素數側

- 類型：`G-INT`, `G-ERR`
- 嚴重度：`S2`
- 義務：導出與 Riemann–Weil 顯式公式兼容的迹公式，並控制正則化與發散項。
- 狀態：`OPEN`

### `RH-HP-05`：非循環構造

- 類型：`G-CIR`
- 嚴重度：`S3`
- 義務：算子不得以「已在臨界線上的零點序列」作為定義資料，再由實譜反推出 RH。
- 狀態：`OPEN`

## 9.3 路線判定

此路線最常見的假完成是：

$$
\text{形式 Hamiltonian}
+\text{數值譜相似}
\not\Rightarrow
\text{Hilbert–Pólya 完成}.
$$

終端 GAP 是自伴性與完整譜雙射的同時建立。

---

# 10. 路線 DBN：de Bruijn–Newman 熱流

## 10.1 已知入口

存在常數 $\Lambda$，使 $H_t$ 全部零點為實數恰當且僅當 $t\geq\Lambda$。已知：

$$
RH\Longleftrightarrow\Lambda\leq0,
$$

且 Rodgers–Tao 證明：

$$
\Lambda\geq0.
$$

因此：

$$
RH\Longleftrightarrow\Lambda=0.
$$

## 10.2 GAP 登錄

### `RH-DBN-01`：終端上界

- 類型：`G-EQV`
- 嚴重度：`S3`
- 義務：證明

$$
\Lambda\leq0.
$$

- 狀態：`EQUIVALENT_RISK`

### `RH-DBN-02`：局部零點動力到全域閾值

- 類型：`G-UNI`, `G-DOM`
- 嚴重度：`S3`
- 義務：把有限高度的零點追蹤、近碰撞或 Lehmer pair 資訊，提升為對全部高度與整條熱流的控制。
- 狀態：`OPEN`

### `RH-DBN-03`：近碰撞資訊的方向性

- 類型：`G-INT`
- 嚴重度：`S2`
- 義務：明確區分哪些結構只能改進 $\Lambda$ 的下界，哪些可能提供上界。不能以證明 $\Lambda\geq c$ 的機制反向宣稱 $\Lambda\leq0$。
- 狀態：`OPEN`

### `RH-DBN-04`：有限計算證書

- 類型：`G-NUM`, `G-CER`
- 嚴重度：`S2`
- 義務：區間算術可證明有限區域零點性質或改進上界，但必須標示其全域延伸所需的解析尾界。
- 狀態：`OPEN`

---

# 11. 路線 EF：顯式公式與素數誤差項

## 11.1 已知入口

RH 與若干素數計數誤差的平方根尺度控制等價或緊密等價，例如對 Chebyshev 函數的典型形式：

$$
\psi(x)=x+O\!\left(x^{1/2}\log^2x\right).
$$

具體對數次方取決於使用的等價版本與正規化。

## 11.2 GAP 登錄

### `RH-EF-01`：平方根抵消

- 類型：`G-ERR`, `G-EQV`
- 嚴重度：`S3`
- 義務：無條件把誤差壓到 RH 所需尺度。
- 狀態：`EQUIVALENT_RISK`

### `RH-EF-02`：顯式公式截斷

- 類型：`G-ERR`, `G-UNI`
- 嚴重度：`S2`
- 義務：同時控制零點截斷、水平選擇、平滑化與素數側尾項，且常數對所需範圍一致。
- 狀態：`OPEN`

### `RH-EF-03`：平均結果到逐點結果

- 類型：`G-UNI`, `G-DOM`
- 嚴重度：`S2`
- 義務：平均、幾乎處處或密度結果不能直接升格為每個 $x$ 的界。
- 狀態：`OPEN`

### `RH-EF-04`：局部素數資料到全域零點排除

- 類型：`G-INT`
- 嚴重度：`S3`
- 義務：有限素數表或有限區間誤差不排除極高處的離軸零點。
- 狀態：`OPEN`

---

# 12. 路線 SP：Speiser 導數零點判準

## 12.1 已知入口

Speiser 定理將 RH 等價連到 $\zeta'(s)$ 在臨界線左側是否存在非實零點。

## 12.2 GAP 登錄

### `RH-SP-01`：全域臨界點排除

- 類型：`G-EQV`, `G-UNI`
- 嚴重度：`S3`
- 義務：證明 $\zeta'$ 在指定半平面的全部非實零點均不存在。
- 狀態：`EQUIVALENT_RISK`

### `RH-SP-02`：局部映射幾何到全域排除

- 類型：`G-INT`, `G-DOM`
- 嚴重度：`S2`
- 義務：從局部共形映射、水平集或數值相圖，建立可全域排除導數零點的定理。
- 狀態：`OPEN`

### `RH-SP-03`：零點與臨界點多重度

- 類型：`G-DOM`, `G-COR`
- 嚴重度：`S2`
- 義務：處理重零點、近重零點與導數零點的多重度對應。
- 狀態：`OPEN`

---

# 13. 路線 RMT：隨機矩陣與零點統計

## 13.1 已知入口

黎曼零點的局部統計與隨機矩陣譜統計呈現深刻一致性；這提供強啟發與大量可檢驗預測。

## 13.2 GAP 登錄

### `RH-RMT-01`：統計律不定位單點實部

- 類型：`G-INT`
- 嚴重度：`S3`
- 義務：建立從零點相關函數、間距分布或譜統計到「沒有離軸零點」的確定性定理。
- 狀態：`OPEN`

### `RH-RMT-02`：零密度例外

- 類型：`G-UNI`, `G-DOM`
- 嚴重度：`S3`
- 義務：即使幾乎全部零點服從某統計律，也必須排除密度為零但無限多的離軸例外。
- 狀態：`OPEN`

### `RH-RMT-03`：模型—算術精確對應

- 類型：`G-COR`, `G-SPC`
- 嚴重度：`S2`
- 義務：說明隨機矩陣是極限統計模型、有效近似，或某真正算子的譜；三者不可混同。
- 狀態：`OPEN`

---

# 14. 路線 AD：Adelic／Connes／半局部迹公式

## 14.1 候選入口

此類路線把顯式公式理解為迹公式或吸收譜，並將 Weil 正性翻譯到半局部或非交換幾何結構。

## 14.2 GAP 登錄

### `RH-AD-01`：空间與迹的嚴格定義

- 類型：`G-DEF`, `G-SPC`
- 嚴重度：`S2`
- 義務：固定商空間、作用、Hilbert 空間、正則化迹與測試函數類。
- 狀態：`OPEN`

### `RH-AD-02`：半局部正性到全域正性

- 類型：`G-POS`, `G-UNI`, `G-CLS`
- 嚴重度：`S3`
- 義務：把有限素數集合 $S$ 上的半局部結構，以一致方式推至全部 places，並保持 Weil 型正性。
- 狀態：`OPEN`

### `RH-AD-03`：缺失譜／吸收譜的完整性

- 類型：`G-COR`, `G-SPC`
- 嚴重度：`S3`
- 義務：證明所有且只有非平凡零點以正確多重度出現在譜機制中。
- 狀態：`OPEN`

---

# 15. 路線 OD：觀察框架、參數化表示與動態投影

此路線來自四份舊稿清理後保留的研究初心。它不是 RH 等價判準，而是候選發現工具。

## 15.1 GAP 登錄

### `RH-OD-01`：操作分類

- 類型：`G-DEF`, `G-INV`
- 嚴重度：`S1`
- 義務：每個操作必須分類為座標變換、表示變換、函數形變、解析延拓或數值近似。
- 狀態：`OPEN`

### `RH-OD-02`：非平凡性

- 類型：`G-INV`
- 嚴重度：`S2`
- 義務：排除候選族只是

$$
F_\theta=F_0\circ T_\theta
$$

所造成的零點逆像搬移。
- 狀態：`OPEN`

### `RH-OD-03`：指標—RH 接口

- 類型：`G-INT`, `G-EQV`
- 嚴重度：`S3`
- 義務：對任何「清晰度、規律性、熵、條件數、最優角度」指標 $J(\theta)$，建立獨立定理：

$$
\mathcal P(J)
\Longrightarrow
\text{RH 的已知必要條件、充分條件或等價條件}.
$$

- 狀態：`OPEN`

### `RH-OD-04`：重新參數化不變性

- 類型：`G-INV`
- 嚴重度：`S2`
- 義務：若最優點可因任意參數重標而搬移，則「最佳角度」沒有內在意義。需指定幾何、測度或自然參數化。
- 狀態：`OPEN`

### `RH-OD-05`：資料洩漏與種子偏誤

- 類型：`G-NUM`, `G-CER`
- 嚴重度：`S1`
- 義務：不得以已知臨界線零點作種子，再以輸出集中於臨界線作為發現。
- 狀態：`OPEN`

## 15.2 路線判定

此路線目前只能作為：

- 候選不變量生成器；
- 數值條件數比較器；
- 形變族探索器；
- 反例與座標幻覺測試器。

在 `RH-OD-03` 回填以前，任何最優化結果都不能作為 RH 證據。

---

# 16. 路線 NUM：有限高度驗證與嚴格計算

## 16.1 已知入口

區間算術、Turing 方法與零點計數可嚴格驗證有限高度內的零點均位於臨界線。

## 16.2 GAP 登錄

### `RH-NUM-01`：有限高度到無限高度

- 類型：`G-NUM`, `G-DOM`
- 嚴重度：`S3`
- 義務：不存在僅由「驗證到更高」自動得到全域 RH 的步驟；需另有解析尾定理。
- 狀態：`OPEN`

### `RH-NUM-02`：邊界無零點證書

- 類型：`G-CER`
- 嚴重度：`S1`
- 義務：輻角積分必須證明邊界上無零點，並給出積分與捨入誤差界。
- 狀態：`OPEN`

### `RH-NUM-03`：高精度不等於嚴格

- 類型：`G-CER`
- 嚴重度：`S1`
- 義務：一般浮點 `mpmath` 結果只能標 `REPRODUCED` 或 `EXPERIMENTAL`；只有區間／球算術與證書可標 `CERTIFIED_NUMERICAL`。
- 狀態：`OPEN`

---

# 17. 路線 FORM：形式化證明工程

形式化不是新的 RH 路線，但它是 GAP 審計層。

### `RH-FORM-01`：定義庫缺口

- 類型：`G-FRM`
- 嚴重度：`S1–S2`
- 義務：確認完成 zeta、顯式公式、測試函數空間、二次型與閉算子的形式化可用程度。
- 狀態：`OPEN`

### `RH-FORM-02`：自然語言到 Lean 的語義保持

- 類型：`G-SEM`, `G-FRM`
- 嚴重度：`S2`
- 義務：每個候選橋樑需有唯一或有限候補的形式化版本，避免在翻譯時改變命題。
- 狀態：`OPEN`

### `RH-FORM-03`：未證引理封裝

- 類型：`G-CIR`, `G-FRM`
- 嚴重度：`S2`
- 義務：禁止把主要 GAP 寫成 theorem 參數、axiom 或 `sorry` 後，再宣稱下游定理完成。
- 狀態：`OPEN`

### `RH-FORM-04`：依賴祖先審計

- 類型：`G-DEP`, `G-CIR`
- 嚴重度：`S2`
- 義務：自動檢查

$$
RH\notin\operatorname{Anc}(M_i)
$$

及所有等價命題的污染。
- 狀態：`OPEN`

---

# 18. 首輪跨路線核心 GAP

把上述路線壓縮後，真正反覆出現的不是數百個無關問題，而是七種母缺口。

## `META-GAP-1`：等價重述沒有負擔下降

$$
P\Longleftrightarrow M
$$

不代表 $M$ 比 $P$ 容易。需衡量：

$$
C(M)<C(P)?
$$

其中 $C$ 可包含最大局部證明負擔、函數空間複雜度、全域量詞與可形式化程度。

## `META-GAP-2`：局部結果無法全域化

常見形式：

$$
\forall T<\infty,\ P(T)
$$

不自動推出：

$$
P(\infty).
$$

## `META-GAP-3`：平均／統計無法排除稀薄例外

$$
\text{密度一成立}
\not\Rightarrow
\text{全部成立}.
$$

## `META-GAP-4`：正性需要控制無限族

Weil、Li、迹公式與算子路線最終常收斂到：

$$
\forall x\in\mathcal X,
\quad Q(x)\geq0.
$$

問題不只是計算，而是找到能保存正性的生成族、分解與閉包。

## `META-GAP-5`：譜類比缺少精確算子

「像譜」與「是某自伴算子的完整譜」之間隔著：

- 定義域；
- 自伴性；
- 譜型；
- 多重度；
- 完備對應；
- 迹公式。

## `META-GAP-6`：數值證據缺少解析尾橋

有限計算的價值很高，但其合法結論是有限區域證書、界的改善或反例搜尋，不是無限命題。

## `META-GAP-7`：中介命題可能偷渡目標

越接近終點的漂亮橋樑，越需要檢查：

$$
M\approx RH?
$$

以及：

$$
RH\in\operatorname{Anc}(M)?
$$

---

# 19. AMRAL 的 GAP 驅動執行規格

## 19.1 每輪只選一條邊

不得下達：「證明 RH」。

應下達：

> 對 `RH-W-02`，在固定 Weil 函數空間下，列出三個不以 $Q\geq0$ 定義的候選生成族，並對每一個生成族尋找閉包失敗證人。

## 19.2 每輪輸出

每輪必須產生：

1. 更新後的 GAP 記錄；
2. 新增或刪除的依賴邊；
3. 候選回填引理；
4. 反例／失敗證人；
5. 文獻來源；
6. 計算或形式證書；
7. 循環與等價風險；
8. 下一輪最小任務。

## 19.3 優先級函數

可使用：

$$
\operatorname{Priority}(G)
=
\frac{
I(G)\cdot F(G)\cdot V(G)
}{
C(G)\cdot R(G)
},
$$

其中：

- $I(G)$：對目標的影響；
- $F(G)$：可被回填的可能性；
- $V(G)$：可驗證性；
- $C(G)$：計算／證明成本；
- $R(G)$：循環、污染與等價風險。

這不是客觀數學量，而是研究排程工具。

---

# 20. 第一階段執行順序

## Cycle G0：制度建立

- 固定 GAP schema；
- 建立 JSON／CSV 登錄；
- 建立唯一 ID；
- 禁止未標狀態命題進入主圖。

## Cycle G1：四份舊稿逐句映射

把每一條殘存主張映射到：

- 已知錨點；
- `REFUTED`；
- `EXPERIMENTAL`；
- 某一個 `RH-OD-*` GAP；
- 某一個 `RH-W-*` GAP。

## Cycle G2：Weil 正性路線

優先處理：

$$
RH\text{-W-01},
RH\text{-W-02},
RH\text{-W-05}.
$$

原因：這三者適合函數分析、反例搜尋與形式化，且能先判斷 $B_3$／$B_6$ 是否真有降負擔。

## Cycle G3：Nyman–Beurling 對照組

將閉包與逼近問題作為另一個可計算、可形式化的生成族實驗，對比 Weil 路線的閉包困難。

## Cycle G4：Hilbert–Pólya 反偽證明模板

建立自動審計：

- 是否只證形式對稱；
- 是否先輸入零點；
- 是否缺少譜雙射；
- 是否有額外譜；
- 是否未處理定義域。

## Cycle G5：DBN 與數值證書

將所有結果分成：

- 下界機制；
- 上界機制；
- 有限零點追蹤；
- 全域尾界。

禁止方向混淆。

---

# 21. 本版結論

本版沒有解決任何 RH 終端 GAP，但完成了一項必要的研究前置：

1. 把「黎曼猜想有很多 GAP」改寫成可登錄的缺口類型；
2. 將十個主要入口拆成精確的停止邊；
3. 區分局部技術缺口與實質等價於 RH 的終端缺口；
4. 建立 RIITG 生成、RAB 回填、KCPE 局部搜索與 AMRAL 持續更新的接口；
5. 明確把數值、統計、譜類比與真正定理分層；
6. 為後續 AI 接力建立可累積的失敗與依賴紀錄。

最重要的判斷是：

> 黎曼猜想不是缺少一篇更長的證明稿，而是缺少一張能顯示每條路線在哪裡把局部困難重新聚合成 RH 本身的依賴圖。

從此之後，研究單位不再是「一篇候選證明」，而是：

$$
\text{一條可審計的 GAP 邊}.
$$

---

# 參考資料與方法來源

## EveMissLab 方法論

1. Neo.K／Aletheia，〈從暫態公理到可回填橋樑：黎曼猜想案例中的結果誘導中介命題重建〉，2026。  
   https://logic.evemisslab.com/p/lm-001356/
2. Neo.K／Aletheia，〈結果誘導的中介定理生成法與逆向公理回填法〉，2026。  
   https://logic.evemisslab.com/p/lm-001368/
3. Neo.K／Aletheia，〈自主數學研究代理循環：結果誘導中介定理生成、逆向公理回填與知識條件化類窮舉〉，2026。  
   https://logic.evemisslab.com/p/lm-001369/

## RH 與主要路線

4. Clay Mathematics Institute, *Riemann Hypothesis*.  
   https://www.claymath.org/millennium/riemann-hypothesis/
5. B. Rodgers and T. Tao, *The De Bruijn–Newman Constant Is Non-Negative*, 2018/2020.  
   https://arxiv.org/abs/1801.05914
6. D. H. J. Polymath, *Effective Approximation of Heat Flow Evolution of the Riemann $\xi$ Function, and a New Upper Bound for the de Bruijn–Newman Constant*, 2019.  
   https://arxiv.org/abs/1904.12438
7. J.-F. Burnol, *The Explicit Formula in Simple Terms*, 1998.  
   https://arxiv.org/abs/math/9810169
8. J.-F. Burnol, *A Note on Nyman's Equivalent Formulation of the Riemann Hypothesis*, 1999.  
   https://arxiv.org/abs/math/9910055
9. L. Báez-Duarte, *A Strengthening of the Nyman–Beurling Criterion for the Riemann Hypothesis*, 2002.  
   https://arxiv.org/abs/math/0202141
10. J. C. Lagarias, *Li Coefficients for Automorphic L-Functions*, 2004.  
    https://arxiv.org/abs/math/0404394
11. A. Connes, *An Essay on the Riemann Hypothesis*, 2015.  
    https://arxiv.org/abs/1509.05576
12. D. Platt and T. Trudgian, *The Riemann Hypothesis Is True up to $3\cdot10^{12}$*, 2020/2021.  
    https://arxiv.org/abs/2004.09765

