# RH-W-02：Weil 測試函數核心、值域與拓撲
## Riemann Hypothesis GAP Engineering Note v0.1

**研究計畫：** RH GAP Atlas / AI 數學工程化接力  
**父節點：** `RH-W-02`  
**前置節點：** `RH-W-01`  
**狀態：** `CORE_CLOSED / GLOBAL_BRIDGE_OPEN`  
**日期：** 2026-07-23  
**性質：** 函數空間與閉包工程；不是 RH 證明，不建立新的 Weil 正性結果

---

# 0. 本輪結論

令

$$
D=x\frac{d}{dx},
\qquad
\mathcal A=D(D+1),
$$

並定義緊支撐平滑雙消失矩核心：

$$
\mathcal C_{00}
:=
\left\{
 g\in C_c^\infty(0,\infty):
 \widetilde g(0)=\widetilde g(1)=0
\right\}.
$$

本輪證明：

$$
\boxed{
\mathcal A C_c^\infty(0,\infty)=\mathcal C_{00}
}.
$$

所以 `RH-W-01` 建立的解析生成核心

$$
\mathcal G_{\mathrm{bump}}
:=D(D+1)C_c^\infty(0,\infty)
$$

並不是只覆蓋部分合法函數，而是**精確覆蓋全部緊支撐平滑、雙消失矩的測試函數**。

同時，本輪在 $C_c^\infty$ 的 LF 拓撲下完成：

$$
\text{原子字典稠密}
\quad+
\quad Q_{B0}\text{ 連續}
\quad\Longrightarrow\quad
\text{字典上的正性可傳到 }\mathcal C_{00}.
$$

然而這仍不等於 RH。真正未完成的橋是：

$$
\mathcal C_{00}
\longrightarrow
\text{一個已知與 RH 等價的完整 Weil 測試空間}.
$$

---

# 1. 三層空間，不得混用

## 1.1 核心層

$$
\mathcal C_{00}
\subset C_c^\infty(0,\infty).
$$

此層優點：

- 算術和有限；
- Mellin 變換整函數且垂直快速衰減；
- 零點和絕對收斂；
- 所有相關函數與微分操作都可在經典函數層處理；
- 適合程式、CAS 與形式化。

## 1.2 B0 廣義層

Bombieri／Clay 的基準類為衰減型函數空間 $\mathcal W$。Weil 判準對滿足兩個消失矩的 $g\in\mathcal W$ 表述。這一層包含不緊支撐函數，故算術和、零點和與尾部控制不再自動有限。

## 1.3 帶狀解析完成層

Lagarias 在 Mellin 側使用帶狀解析測試函數空間 $\mathcal A_\delta$，以閉帶上的一致範數作為拓撲；在無條件情況下，$\delta>\tfrac12$ 時 Weil 分布可作為連續線性泛函，且 Weil 判準可在適當的 $\mathcal A_\delta$ 上表述。

本工程暫將其視為候選全域目標：

$$
\widehat{\mathcal A}_{\delta,00}
:=
\left\{
F\in\widehat{\mathcal A}_\delta:
F(0)=F(1)=0
\right\},
\qquad \delta>\frac12.
$$

但從 $\mathcal C_{00}$ 到此空間的稠密性與正規化一致性，尚未在本工程內證明。

---

# 2. 對數座標

令

$$
x=e^u,
\qquad
G(u):=g(e^u),
\qquad
H(u):=h(e^u).
$$

則：

$$
D\longleftrightarrow\partial_u,
$$

且

$$
D(D+1)h
\longleftrightarrow
P H:=\partial_u(\partial_u+1)H
=H''+H'.
$$

兩個 Mellin 消失矩變成：

$$
\widetilde g(0)=0
\Longleftrightarrow
\int_{\mathbb R}G(u)\,du=0,
$$

$$
\widetilde g(1)=0
\Longleftrightarrow
\int_{\mathbb R}e^uG(u)\,du=0.
$$

定義：

$$
\mathscr D_{00}
:=
\left\{
G\in C_c^\infty(\mathbb R):
\int G(u)\,du=0,
\ \int e^uG(u)\,du=0
\right\}.
$$

問題因此化為：

$$
P C_c^\infty(\mathbb R)
\stackrel{?}{=}
\mathscr D_{00}.
$$

---

# 3. 精確值域定理

## 定理 3.1

$$
\boxed{
P C_c^\infty(\mathbb R)=\mathscr D_{00}
}.
$$

而且 $P$ 在 $C_c^\infty(\mathbb R)$ 上單射，因此：

$$
P:C_c^\infty(\mathbb R)
\longrightarrow
\mathscr D_{00}
$$

為線性雙射。

## 3.1 必要性

若

$$
G=H''+H',
\qquad H\in C_c^\infty(\mathbb R),
$$

則：

$$
\int_{\mathbb R}G(u)\,du
=
\int H''(u)\,du+
\int H'(u)\,du
=0.
$$

另一方面：

$$
\int_{\mathbb R}e^uG(u)\,du
=
\int e^u(H''+H')\,du.
$$

注意：

$$
\frac{d}{du}\bigl(e^uH'(u)\bigr)
=e^u(H''+H'),
$$

所以：

$$
\int e^uG(u)\,du=0.
$$

故：

$$
P C_c^\infty(\mathbb R)
\subseteq\mathscr D_{00}.
$$

## 3.2 充分性與顯式反演

現在取任意：

$$
G\in\mathscr D_{00}.
$$

先定義：

$$
Y(u)
:=
e^{-u}
\int_{-\infty}^{u}e^vG(v)\,dv.
$$

直接微分得：

$$
Y'(u)+Y(u)=G(u).
$$

因：

$$
\int_{\mathbb R}e^vG(v)\,dv=0,
$$

當 $u$ 超過 $G$ 的支撐右端時，積分為零；當 $u$ 位於支撐左側時積分也為零。因此：

$$
Y\in C_c^\infty(\mathbb R).
$$

再由 $Y'+Y=G$ 積分：

$$
\int_{\mathbb R}Y(u)\,du
=
\int_{\mathbb R}G(u)\,du
=0.
$$

定義：

$$
H(u):=
\int_{-\infty}^{u}Y(v)\,dv.
$$

因 $Y$ 緊支撐且總積分為零，故：

$$
H\in C_c^\infty(\mathbb R),
\qquad H'=Y.
$$

最後：

$$
P H
=H''+H'
=Y'+Y
=G.
$$

因此：

$$
\mathscr D_{00}
\subseteq
P C_c^\infty(\mathbb R).
$$

## 3.3 唯一性

若：

$$
P H=0,
$$

則：

$$
H''+H'=0,
$$

所以：

$$
H(u)=c_0+c_1e^{-u}.
$$

唯一可能緊支撐的解是：

$$
H=0.
$$

故 $P$ 單射。

---

# 4. 乘法座標中的反演公式

對：

$$
g\in\mathcal C_{00},
$$

先定義：

$$
y(x)
:=
\frac1x\int_0^x g(t)\,dt.
$$

則：

$$
(D+1)y=g.
$$

再定義：

$$
h(x)
:=
\int_0^x y(t)\frac{dt}{t}.
$$

則：

$$
Dh=y,
$$

從而：

$$
D(D+1)h
=(D+1)Dh
=(D+1)y
=g.
$$

兩個消失矩恰好保證 $y$ 與 $h$ 在支撐右側重新回到零，所以 $h$ 仍為緊支撐平滑函數。

**工程意義：** 每個合法核心輸入 $g$ 都有唯一種子 $h$，而不是只有部分 $g$ 能由算子生成。

---

# 5. 支撐保持與拓撲同構

若：

$$
\operatorname{supp}(G)\subseteq[a,b],
$$

則上述反演給出：

$$
\operatorname{supp}(Y)
\subseteq[a,b],
\qquad
\operatorname{supp}(H)
\subseteq[a,b].
$$

所以 $P$ 不只保持緊支撐，反算子也不需要擴張支撐。

對固定緊區間 $K$，令：

$$
\mathscr D_K=C_K^\infty(\mathbb R),
$$

配備標準 Fréchet 半範數：

$$
p_m(F)=\max_{0\leq j\leq m}
\sup_{u\in K}|F^{(j)}(u)|.
$$

由積分反演公式，對每個 $m$ 存在依賴於 $K,m$ 的常數 $C_{K,m}$，使：

$$
p_m(H)
\leq
C_{K,m}
\,p_{m-1}(G)
$$

或在統一索引後寫成：

$$
p_m(H)
\leq
C'_{K,m}p_m(G).
$$

而 $P$ 顯然是連續微分算子。因此：

$$
P:\mathscr D_K
\longrightarrow
\mathscr D_{00,K}
$$

是 Fréchet 空間間的拓撲同構。

對所有緊集取嚴格歸納極限，得到：

$$
P:C_c^\infty(\mathbb R)
\longrightarrow
\mathscr D_{00}
$$

是 LF 空間層級的拓撲同構。

---

# 6. 固定 bump 原子字典的稠密性

上一輪程式使用固定平滑 bump 的平移、縮放、調制與有限線性組合。現在區分：

## 6.1 解析完整族

$$
\mathcal G_{\mathrm{core}}
:=P C_c^\infty(\mathbb R)
=\mathscr D_{00}.
$$

此族已精確等於完整核心，不需要稠密性論證。

## 6.2 可計算原子字典

令 $\eta\in C_c^\infty(\mathbb R)$ 為固定非零 bump，考慮種子原子：

$$
\eta_{\mu,\sigma}(u)
:=
\eta\!\left(\frac{u-\mu}{\sigma}\right),
\qquad \sigma>0.
$$

令：

$$
\mathscr A_\eta
:=
\operatorname{span}_{\mathrm{fin}}
\left\{
\eta_{\mu,\sigma}:
\mu\in\mathbb R,
\sigma>0
\right\}.
$$

標準 mollifier 逼近給出：

$$
\overline{\mathscr A_\eta}^{\,C_c^\infty}
=C_c^\infty(\mathbb R).
$$

理由是：對任意 $H\in C_c^\infty$，卷積 $H*\eta_\varepsilon$ 在所有導數上一致收斂到 $H$；而每個卷積積分可在任意有限階 $C^m$ 半範數中由有限 Riemann 和逼近。以對角序列同時處理所有 $m$，得到 LF 收斂。

因 $P$ 連續且滿射到 $\mathscr D_{00}$：

$$
\boxed{
\overline{P\mathscr A_\eta}^{\,\mathscr D_{00}}
=
\mathscr D_{00}
}.
$$

調制參數 $e^{i\tau u}$ 對稠密性不是必要條件，但可增加搜尋字典的頻率局部化能力。

---

# 7. B0 算術泛函在核心上的連續性

定義：

$$
f_g(x)
=
\int_0^\infty
 g(xy)\overline{g(y)}\,dy,
$$

以及：

$$
Q_{B0}(g)
:=-E_{\mathrm{arith}}(f_g).
$$

## 7.1 相關映射連續

在固定支撐層：

$$
g\mapsto f_g
$$

是連續二次映射。若 $g$ 支撐於 $[a,b]$，則 $f_g$ 支撐於 $[a/b,b/a]$，且對每個 $m$ 有：

$$
p_m(f_g)
\leq
C_{a,b,m}\,p_m(g)^2.
$$

更一般的雙線性極化：

$$
f_{g,h}(x)
:=
\int_0^\infty g(xy)\overline{h(y)}\,dy
$$

滿足：

$$
p_m(f_{g,h})
\leq
C_{a,b,m}p_m(g)p_m(h).
$$

## 7.2 顯式公式算術側為連續分布

對固定緊支撐 $L\subset(0,\infty)$：

- von Mangoldt 和只有有限項；
- 點值 $f(n)$、$f(1/n)$ 與 $f(1)$ 是連續線性泛函；
- 阿基米德積分在 $x=1$ 的表面奇異由一階消去，故可由 $C^1$ 半範數控制；
- 支撐以外沒有尾項。

因此存在常數 $C_L$ 使：

$$
|E_{\mathrm{arith}}(f)|
\leq
C_L\bigl(p_0(f)+p_1(f)\bigr).
$$

所以：

$$
E_{\mathrm{arith}}:
C_c^\infty(0,\infty)
\longrightarrow\mathbb C
$$

是 LF 連續線性泛函。

合成後：

$$
Q_{B0}:\mathcal C_{00}\longrightarrow\mathbb R
$$

是連續二次型。

---

# 8. 合法的閉包傳遞

令：

$$
\mathcal D_\eta:=P\mathscr A_\eta.
$$

已知：

$$
\overline{\mathcal D_\eta}^{\,\mathcal C_{00}}
=
\mathcal C_{00},
$$

且 $Q_{B0}$ 連續。因此若未來能證明：

$$
\forall g\in\mathcal D_\eta,
\qquad Q_{B0}(g)\geq0,
$$

則對任意 $g\in\mathcal C_{00}$，取 $g_n\in\mathcal D_\eta$ 且 $g_n\to g$：

$$
Q_{B0}(g)
=
\lim_{n\to\infty}Q_{B0}(g_n)
\geq0.
$$

因此：

$$
\boxed{
Q_{B0}\geq0\text{ on }\mathcal D_\eta
\Longrightarrow
Q_{B0}\geq0\text{ on }\mathcal C_{00}
}.
$$

這修正了舊稿中模糊的「用下半連續性傳遞正性」問題；本層使用的是明確的二次型連續性。

---

# 9. 為何裸 $L^2$ 不是合法的無條件完成

Mellin–Plancherel 給出：

$$
L^2\!\left((0,\infty),\frac{dx}{x}\right)
\cong
L^2\!\left(\frac12+i\mathbb R,\frac{dt}{2\pi}\right).
$$

但不能因此直接把 Weil 二次型延拓到裸 $L^2$。

原因一：$L^2$ 元素只是幾乎處處等價類，單點值沒有定義。

原因二：單點求值在 $L^2(\mathbb R)$ 上不連續。取固定平滑 $\psi$ 且 $\psi(0)=1$，令：

$$
\psi_n(t):=\psi(n(t-t_0)).
$$

則：

$$
\psi_n(t_0)=1,
$$

但：

$$
\|\psi_n\|_{L^2}
=n^{-1/2}\|\psi\|_{L^2}
\longrightarrow0.
$$

Weil 泛函涉及在零點位置的解析函數值；若沒有 Hardy、Sobolev 或帶狀全純結構，這些值不能由裸 $L^2$ 範數控制。

所以：

$$
\boxed{
\text{裸 }L^2\text{ 完成被拒絕為無條件 Weil 完成空間}
}.
$$

Lagarias 使用帶狀全純函數及閉帶一致範數，正是為了保留解析延拓與點值控制，而不只是保留臨界線上的 $L^2$ 類。

---

# 10. 尚未跨越的全域橋

本輪只證明：

$$
\text{原子字典}
\longrightarrow
\mathcal C_{00}
$$

的閉包傳遞。

尚未證明：

$$
\overline{\widehat{\mathcal C}_{00}}^{\,\|\cdot\|_{\infty,S_\delta}}
=
\widehat{\mathcal A}_{\delta,00},
\qquad \delta>\frac12.
$$

這個命題並非形式上的「平滑函數通常稠密」；一致範數作用在無界閉帶，而且要求全純性、垂直方向衰減、$s=0,1$ 消零與無條件零點求值同時相容。

因此下一個真正 GAP 是：

$$
\boxed{
\texttt{RH-W-02-GLOBAL-DENSITY}
}
$$

其證明義務為：

1. 精確固定 $\mathcal A_\delta$ 的完整定義與成長條件；
2. 固定 B0 與 Lagarias covariance normalization 的轉換；
3. 證明緊支撐 Mellin 像在雙消零子空間中的稠密性，或找到較小但仍與 RH 等價的完備核心；
4. 證明 Weil 泛函與二次型在該逼近下連續；
5. 若稠密性失敗，產出不可逼近的失敗證人。

---

# 11. GAP 狀態

| ID | 狀態 | 本輪判定 |
|---|---|---|
| `RH-W-02-RANGE` | `CLOSED` | $D(D+1)C_c^\infty=\mathcal C_{00}$ |
| `RH-W-02-INVERSE` | `CLOSED` | 顯式唯一反算子已給出 |
| `RH-W-02-SUPPORT` | `CLOSED` | 反演保持同一緊支撐區間 |
| `RH-W-02-ATOM-DENSE` | `CLOSED` | bump 原子經 $D(D+1)$ 後在核心稠密 |
| `RH-W-02-Q-LF` | `CLOSED` | $Q_{B0}$ 在核心 LF 拓撲連續 |
| `RH-W-02-TRANSFER-CORE` | `CLOSED_CONDITIONAL` | 字典正性若成立，可傳到完整核心 |
| `RH-W-02-L2` | `REJECTED` | 裸 $L^2$ 無點值控制，不能作無條件完成 |
| `RH-W-02-ADELTA-NORM` | `REFERENCE_AVAILABLE` | Lagarias 提供帶狀一致範數候選 |
| `RH-W-02-GLOBAL-DENSITY` | `OPEN` | 核心到 RH 等價完整空間的密度橋未證 |
| `RH-W-02-NORMALIZATION` | `OPEN_AUDIT` | B0 negativity 與 covariance positivity 需逐項映射 |
| `RH-W-02-RH-SUFFICIENCY` | `BLOCKED_BY_GLOBAL_DENSITY` | 核心正性是否已足以推出 RH 尚未在本工程閉合 |

---

# 12. 本輪沒有證明的事項

本輪沒有證明：

$$
Q_{B0}(g)\geq0
$$

對任何非平凡無限族成立。

也沒有證明：

$$
Q_{B0}\geq0\text{ on }\mathcal C_{00}
\Longrightarrow RH.
$$

本輪完成的是：

- 核心生成族不再只是候選，而是精確完整；
- 核心內的閉包傳遞已合法化；
- 裸 $L^2$ 的錯誤完成方式已排除；
- 真正剩餘的全域密度橋已被單獨登錄。

---

# 13. 下一個接力節點

推薦下一輪優先處理：

$$
\boxed{
\texttt{RH-W-02-NORMALIZATION}
}
$$

先把 Bombieri／Clay 的 trace-negativity 版本與 Lagarias 的 covariance-positivity 版本做成逐項可逆轉換。完成後，再處理：

$$
\boxed{
\texttt{RH-W-02-GLOBAL-DENSITY}
}
$$

否則「核心在何種完成空間中稠密」仍會因對象與符號沒有完全對齊而失真。

---

# 參考基準

1. Enrico Bombieri, “The Riemann Hypothesis,” in *The Millennium Prize Problems*, explicit formula and Weil negativity criterion.
2. Jeffrey C. Lagarias, “Li Coefficients for Automorphic L-Functions,” Appendix 9: strip test spaces, Weil distribution continuity and covariance formulation.
3. Jean-François Burnol, “The Explicit Formula in Simple Terms,” multiplicative convolution and distributional formulation background.
