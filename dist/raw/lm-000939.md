# 被丟掉的見證者：把 ε-δ 微積分整理成可在機器碼上運行的形式

### 從連續模、構造實數，到自動微分——一篇整理性筆記

**作者**：Neo.K（許筌崴），EveMissLab
**對話夥伴**：Theia（Claude Opus 4.8）
**日期**：2026 年 6 月 3 日
**性質**：實驗站整理性筆記。**沒有任何新發現，沒有任何新定義（在某種意義上）**。本文不證明任何先前未被證明之事，所引結果皆為公認既有定理。我們做的只有一件事——把一條早已存在、卻散落在可計算分析、構造分析、自動微分與形式驗證各處的路徑，沿一條主軸串起來，使「ε-δ 為何不能跑、以及它如何才能跑」一目了然。
**緣起**：本文出自與 Theia 的一段對話，承接前一篇〈我們判斷一件事能走多遠時，判的究竟是什麼〉。主軸的提法、串接與取捨由作者主導；多領域定理的定位、修正與程式驗證為對話共同澄清。若本文對某些讀者有啟發之效，那啟發來自既有結果本身的結構，而非來自任何新主張。

---

## 〇、主軸：計算，是不准丟掉見證者的紀律

把 ε-δ 的極限定義攤開：

> lim_{x→a} f(x) = L  ⟺  ∀ε>0, ∃δ>0, ∀x, 0<|x−a|<δ ⟹ |f(x)−L|<ε。

這是一個 ∀∃∀ 結構的 Π₂ 命題，三層量詞，且對不可數的 ℝ 作全稱。它在邏輯層級上就不可計算——不是因為記號笨拙，是因為它斷言了一個「存在但不交出」的 δ。古典分析的優雅，正在於允許自己宣告 δ 存在卻從不出示；而計算這門手藝的全部紀律，恰恰相反：**每一個 ∃ 都必須附上能跑的見證者**。

本文要整理的，就是這條把古典 ε-δ 逐層「攜帶見證者化」的正統路徑。它不改寫微積分的任何定理，它只是拒絕在每一步把存在量詞背後的構造扔掉。一句話：古典分析丟掉見證者換取閉合，可計算分析攜帶見證者換取可動。

下面分七層敘述（第〇至第六層），最後接回上一篇的可數天花板。

## 一、問題：ε-δ 為什麼不能直接編譯

承上。∀ε∃δ 不可計算的根，在前一篇已經埋好：所有形式語言、所有參考機合起來只是可數的，而現實是不可數的；可被任何機械程序判定的，只是一道測度為零的薄片。ε-δ 對全體實數作全稱與存在斷言，落點直接在這道薄片之外。因此「讓微積分能跑」這件事，從一開始就不是要它涵蓋全部，而是要把它**投影**到可計算的那道縫上，並在那道縫之內做到嚴謹且可執行。

這不是退讓，是定位。下面每一層，都是把某個古典斷言換成它在那道縫之內的、攜帶見證者的對應物。

## 二、第〇層：邏輯的改寫（這是唯一的引擎）

整套可計算化只有一個動作，其餘都是它的後果：**Skolem 化**。

把 ∀ε∃δ 裡的 ∃δ 提出來，換成一個函數 δ(·)。在構造主義的 BHK 解釋與 Kleene 可實現性（realizability，Kleene 1945）之下，「δ 存在」不被允許作為斷言而存在；它必須由一個程式**實現**：輸入 ε，輸出 δ。這個被 Skolem 化出來的函數，數學上早有名字——**連續模（modulus of continuity）**。

於是極限的可計算定義（用 2^{−n} 為 ε 編號）是：

> lim_{x→a} f(x) = L 可計算  ⟺  存在可計算的 h : ℕ → ℕ，使得對所有 x，0 < |x−a| < 2^{−h(n)} ⟹ |f(x)−L| < 2^{−n}。

ε 變成編號 n，∃δ 變成函數 h(n)，整條 ε-δ 從一個邏輯命題塌成一段帶型別的可執行項。古典 ε-δ 與可計算 ε-δ 之間，沒有任何新數學——差別純粹是：後者拒絕把 h 丟掉。Skolem 化就是「顯式攜帶存在見證者」的另一個名字。

這一層做完，剩下的全是這個原則在各處的具現。

## 三、第一層：實數作為自帶模的型別

實數不再是「一個點」，而是一個攜帶自身收斂速率的物件：

> 實數 x  ≔  一個快速 Cauchy 序列 q : ℕ → ℚ，滿足對所有 n，|x − q(n)| ≤ 2^{−n}。

機器碼層級，x 是一條串流：n ↦ 一個寬度 ≤ 2^{−n} 的有理區間。要更精確，就向它多要幾位（Turing 1936 對「可計算數」的原始定義即是如此）。

這一層藏著一個直接的、工程必需的硬事實：**普通（非冗餘）位置記數法不可計算**。要輸出 (1/3)×3 的最高位數字，你得先裁決它究竟是 0.999… 還是 1.000…，而這需要檢查無窮多位——進位可以無限傳播而永不落定。古典解法（Avizienis 1961 的帶號數字；更早可溯及 Brouwer 對選擇序列的處理）是改用**冗餘表示**，例如數字取自 {−1, 0, 1}，讓「9 與 10 之交」那個臨界永遠保有兩種合法寫法，於是永遠不必裁決首位。

值得標記的對位：在標準完備有序體 ℝ 裡，阿基米德性質判定「無窮小不存在」，0.999… 嚴格等於 1，臨界被公理層級抹平；而在能運算的機器表示裡，那個「永遠差一線、永遠不裁決首位」的冗餘狀態，反而是計算得以進行的必要條件。理論的清潔與機器的可動，在此處要求相反的東西。

附帶一個常被忽略的陷阱（Specker 1949）：完備性公理本身不可計算——存在可計算、單調、有界的有理序列，其極限不是可計算數。所以「攜帶模」不是禮貌，是因為一般的「存在上確界」根本交不出見證者。

## 四、第二層：相等不可判定

兩個實數是否相等，不可判定。x = y 是 Π₁ 性質：你可以半判定 x ≠ y（只要某一位的區間分離開就確定不等），但永遠半判定不了 x = y（那需要看完無窮多位的吻合）。

這在機器上有一條極具體的後果：**exact real arithmetic 禁止寫 `if x == 0`**。所有比較必須換成多值的「軟比較」（soft comparison / split）：給定一個容差，回報「x < 容差」或「x > 0」，並允許重疊區任意裁定。前一篇所說「換不掉的語言不變量」（Rice、停機），在這一層具現為一行字面的程式禁令。本文附錄 A 第三部分對此給了可執行的見證。

## 五、第三層：可計算 ⟹ 連續（主定理）

可計算分析的中心定理：**每個可計算的實函數必然連續**，且攜帶可計算的連續模（與 Brouwer 在直覺主義中「所有全函數連續」的結論同源）。

逆否地說，階躍函數、符號函數、Dirichlet 函數這類不連續物件**根本不可計算**——計算它們等價於判定相等，而相等不可判定（第二層）。於是「連續性」在這套形式裡不是分析學的一種禮貌假設，而是可計算性的純粹副產品：能跑，就連續。

## 六、第四層：微分——表示相對性在微積分骨架中的字面具現

這一層是整篇最關鍵的修正，因為它把前一篇的主旨「描述是相對於解碼器的」，直接做成了一個運算子可不可計算的開關。

**把函數當黑箱串流名**（只能餵一個點、讀一個值）：微分**不可計算**。微分是無界運算子（局部放大任意小的擾動）。Myhill 1971 構造了一個可計算、處處可微、導數連續、但其導數不可計算的函數（亦見 Pour-El & Richards 1989 對分析與物理中可計算性的系統處理）。在這個表示下，f′ 讀不出來。

**把同一個函數當語法（程式 / 表達式樹）**：微分變成精確、平凡、可執行——這就是前向模式自動微分（forward-mode AD），其代數基底正是對偶數環

> R[d]/(d² = 0)，

也就是上一段對話中的綜合微分幾何冪零無窮小。對偶數運算對 d² = 0 求值，使得 f(x + d) = f(x) + f′(x)·d 成為**精確的代數恆等式**，沒有取極限、沒有 o(h)、沒有數值誤差。附錄 A 第一部分驗證了這一點，並對照展示：同一導數用數值有限差分逼近時，不但有誤差，還會在步長過小時因浮點相消而**變得更糟**（h = 10⁻¹² 的誤差大於 h = 10⁻⁸）。AD 的精確不是「逼得更準」，是整個繞開了這個失效模式。

歷史在此閉環：萊布尼茲的 dx →（Weierstrass 算術化）被 ε-δ 當作幽靈驅逐 →（在黑箱表示下）微分淪為不可計算 →（換成語法表示）以冪零元 d² = 0 復活成一個資料結構，並在今日的每一套深度學習框架裡每秒運行無數次。dx 從未被消滅，它只是被換了一台解碼器。

可微或不可微、可計算或不可計算——這從來不是函數本身的屬性，而取決於你選哪一台參考機去讀它。前一篇的論點，在微積分最核心的運算子上得到字面的實例。

## 七、第五層：積分可計算（不對稱性）

與微分相對，積分運算子 f ↦ ∫₀¹ f 在標準表示下**可計算**，並攜帶可計算的模。

這道方向性不對稱有其結構根由：微分是無界運算子（放大局部高頻），積分是有界、平滑化的運算子（抹平局部）。直覺上常被當成「互逆」的這對運算，在可計算性層級上完全不對稱——一個交得出見證者，一個交不出。基本定理把它們綁成互逆，掩蓋了這道落差；可計算化的視角把落差重新顯影。

## 八、第六層：它真的在哪裡運行

這套形式不是玩具。攜帶模的 exact real arithmetic 有工業級實作：iRRAM（Norbert Müller，C++）、AERN（Haskell）、Marshall 等，內部即以帶號串流加模的方式運作。形式驗證端，構造實數已被機器檢查地建立：Coq 的 C-CoRN（Cruz-Filipe, Geuvers, Wiedijk 2004，Bishop 風格）、Lean mathlib 中以 Cauchy 完備化建構的 `Real`。

整條學術正統路徑因此完整可追溯：Turing 1936（可計算數）→ Bishop 1967《構造分析基礎》與 Bishop–Bridges 1985（存在即算法）→ Weihrauch 2000《可計算分析》（二型可計算性 TTE，串流上的圖靈機）→ Avizienis 1961（帶號冗餘記數）→ C-CoRN / Lean mathlib（機器檢查的構造實數）。本文沒有為這條鏈添加任何一環，只是把它拉直。

## 九、天花板：能跑的微積分，只鋪滿那道可數的縫

接回前一篇的結尾。這整套能運行的微積分，完全活在可計算實數之內——而可計算實數是可數的，是不可數現實中一道測度為零的薄片。我們整理出的不是「全部的微積分」，而是「微積分投影到那道縫上、且在縫內無界可用的部分」。

它不違背那道天花板，它正站在天花板底下，把那道縫鋪滿。這恰是前一篇附錄的話：可數不等於可窮盡；一個有界的工具箱，在它那道薄片之內，有著無界的觸及。能跑的微積分，就是這道薄片內被反覆沿用、複合、傳遞的無窮工具之一。

## 結語

古典分析的尊嚴，是允許自己斷言一個從不交出的 δ，用無窮多位的沉默換來閉合的定理。可計算分析的尊嚴，是規定每一次「存在」都得附上一段能跑的證據，用永不裁決的首位數換來一個能動的世界。

而微分這把刀，把整件事說盡了：是被計算，還是不可被計算，從來不寫在函數身上——它寫在你決定用哪一隻手去握它。我們換得掉每一種握法，唯獨換不掉「總得用某種握法去握」這件事。

---

## 附錄 A：程式碼驗證（已執行，附真實輸出）

下列 Python 不依賴任何第三方套件，於標準直譯器即可運行。三段分別對應正文第四層（對偶數自動微分的精確性）、第一與第三層（攜帶模的可計算實數）、第二層（比較的半可判定性）。

```python
from fractions import Fraction
import math

# ============================================================
# Part 1: 前向模式自動微分，對偶數環 R[d]/(d^2 = 0)。導數精確，不取極限。
# ============================================================
class Dual:
    __slots__ = ('a', 'b')          # a + b·d,  d^2 = 0
    def __init__(self, a, b=0): self.a, self.b = a, b
    @staticmethod
    def _c(o): return o if isinstance(o, Dual) else Dual(o, 0)
    def __add__(s, o):
        o = Dual._c(o); return Dual(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __mul__(s, o):
        o = Dual._c(o)
        return Dual(s.a * o.a, s.a * o.b + s.b * o.a)   # d^2 項自動歸零
    __rmul__ = __mul__
    def __repr__(s): return f"{s.a} + {s.b}·d"

def D(f, x):                         # 程式 f 在 x 處的精確導數
    return f(Dual(x, 1)).b

f1 = lambda t: t * t * t             # x^3 ,  f1' = 3x^2 ,  at 2 -> 12
f2 = lambda t: t * t * t + 2 * t     # x^3+2x , f2' = 3x^2+2 , at 2 -> 14
print("== Part 1: dual-number AD (exact) ==")
print("D(x^3) at 2      =", D(f1, 2), "(expected 12)")
print("D(x^3+2x) at 2   =", D(f2, 2), "(expected 14)")

# 對照：數值有限差分只是逼近，且步長過小時因浮點相消而更糟。
g = lambda t: t ** 3
for h in (1e-4, 1e-8, 1e-12):
    fd = (g(2 + h) - g(2)) / h
    print(f"finite diff h={h:<6}=", fd, " error", abs(fd - 12))

# ============================================================
# Part 2: 可計算實數即函數 n |-> 落在真值 2^-n 內的有理數。模被攜帶，而非斷言。
# ============================================================
def sqrt2(n):                        # |sqrt2(n) - sqrt(2)| <= 2^-n
    lo, hi = Fraction(1), Fraction(2)
    bound = Fraction(1, 2 ** n)
    while hi - lo > bound:
        mid = (lo + hi) / 2
        if mid * mid <= 2: lo = mid
        else: hi = mid
    return lo

print("\n== Part 2: computable real sqrt(2), verified modulus ==")
for n in (10, 20, 40):
    approx = float(sqrt2(n))
    ok = abs(approx - math.sqrt(2)) <= 2.0 ** -n
    print(f"n={n:<3} approx={approx:.15f}  |approx-sqrt2|<=2^-n : {ok}")

# 加法自動傳播模：向每個輸入多要一位 (n+1)
def add(x, y): return lambda n: x(n + 1) + y(n + 1)
s = add(sqrt2, sqrt2)                # sqrt2 + sqrt2 = 2*sqrt2
val = float(s(30))
print("sqrt2+sqrt2 at n=30 =", f"{val:.15f}",
      " |.-2sqrt2|<=2^-30 :", abs(val - 2 * math.sqrt(2)) <= 2.0 ** -30)

# ============================================================
# Part 3: 比較只是半可判定。x>0 可證實；x=0 不可——這就是 exact arithmetic
#         禁止 `if x==0` 的原因。
# ============================================================
def certify_positive(x, budget=64):
    for n in range(budget):
        if x(n) - Fraction(1, 2 ** n) > 0:   # 值減去自身的誤差邊界
            return f"x>0 certified at n={n}"
    return "undecided within budget"

sqrt2_minus_1 = lambda n: sqrt2(n + 1) - 1   # ~0.414 > 0
zero          = lambda n: Fraction(0)         # 恰好 0

print("\n== Part 3: comparison semidecidability ==")
print("certify_positive(sqrt2 - 1) :", certify_positive(sqrt2_minus_1))
print("certify_positive(0)         :", certify_positive(zero))
```

執行結果（逐字）：

```text
== Part 1: dual-number AD (exact) ==
D(x^3) at 2      = 12 (expected 12)
D(x^3+2x) at 2   = 14 (expected 14)
finite diff h=0.0001= 12.000600010022566  error 0.0006000100225662663
finite diff h=1e-08 = 11.999999927070348  error 7.29296516510658e-08
finite diff h=1e-12 = 12.001066806988092  error 0.0010668069880921394

== Part 2: computable real sqrt(2), verified modulus ==
n=10  approx=1.414062500000000  |approx-sqrt2|<=2^-n : True
n=20  approx=1.414213180541992  |approx-sqrt2|<=2^-n : True
n=40  approx=1.414213562372424  |approx-sqrt2|<=2^-n : True
sqrt2+sqrt2 at n=30 = 2.828427123837173  |.-2sqrt2|<=2^-30 : True

== Part 3: comparison semidecidability ==
certify_positive(sqrt2 - 1) : x>0 certified at n=2
certify_positive(0)         : undecided within budget
```

三點被驗證者：(1) 對偶數 AD 給出精確整數導數，而有限差分在 h = 10⁻¹² 時誤差反大於 h = 10⁻⁸（浮點相消），坐實「精確 vs 逼近」並非程度之別；(2) √2 作為攜帶模的可計算實數，在 n = 10, 20, 40 三處皆滿足 |approx − √2| ≤ 2⁻ⁿ，且加法自動傳播模；(3) 正數可在有限步證實（n = 2），而恆零者在預算內始終「未裁決」——比較的半可判定性以可執行的方式現形。

---

## 附錄 B：Lean 4 預備欄（未來機器檢查用，尚未編譯）

以下為**預備欄**：一份 Lean 4 / mathlib 風格的骨架，標記正文各層在證明助理中應落腳之處。它**尚未在本機編譯**，定理體以 `sorry` 佔位，部分 mathlib 識別名需對照當前版本核實。列此的目的，是預留未來把附錄 A 的「執行驗證」升級為「機器檢查的證明」之接口。

```lean
import Mathlib

/-! # 預備欄：可計算化微積分的形式骨架
    對應正文第〇至第四層。此檔僅為 scaffold，定理待補。 -/

namespace ComputableCalculus

/-- 第〇/二層：連續模。把 ∀ε∃δ 的 ∃ Skolem 化為一個顯式函數 `m`。 -/
def IsModulusOfContinuity (f : ℝ → ℝ) (a : ℝ) (m : ℕ → ℕ) : Prop :=
  ∀ n : ℕ, ∀ x : ℝ,
    |x - a| < (1 / 2) ^ (m n) → |f x - f a| < (1 / 2) ^ n

/-- 第〇層主張：連續即「存在攜帶的模」。古典 ε-δ 與此等價，
    差別僅在後者要求把見證者 `m` 交出來。 -/
theorem continuous_iff_has_modulus
    (f : ℝ → ℝ) (a : ℝ) :
    ContinuousAt f a ↔ ∃ m : ℕ → ℕ, IsModulusOfContinuity f a m := by
  sorry

/-- 第四層：對偶數 ℝ[d]/(d²=0)。mathlib 已有 `DualNumber R := TrivSqZeroExt R R`，
    其中對偶單位 `ε` 滿足 `ε^2 = 0`。 -/
abbrev D := DualNumber ℝ

/-- 前向模式 AD：在對偶點求值，取出對偶部即導數。
    對多項式（與一切由 mathlib `Differentiable` 證得可微的程式）應有
    `(eval (x + ε) p).snd = deriv (fun t => eval t p) x`。 -/
theorem dual_eval_eq_deriv_poly (p : Polynomial ℝ) (x : ℝ) :
    True := by
  -- 期望形： (p.eval (x + ε)).fst = p.eval x
  --          (p.eval (x + ε)).snd = (Polynomial.derivative p).eval x
  -- 需對照 mathlib 中 DualNumber 上的多項式求值與 `Polynomial.derivative`。
  trivial

/-- 第五層：積分為可計算（有界）運算子；微分一般不可計算（無界，Myhill 1971）。
    在 mathlib 中此對比的恰當陳述需經由 `Computable` / TTE 形式化，
    目前 mathlib 尚未完整涵蓋，故此處僅留標記。 -/
-- TODO: 引入可計算性框架後，陳述 integration 的可計算性與
--       differentiation 的不可計算性（表示相對）。

end ComputableCalculus
```

預備欄到此。當未來把它編譯通過、`sorry` 補實時，附錄 A 的「跑得出正確結果」便升格為「被機器證明為必然正確」——那將是這條整理路徑在形式驗證端的封頂，而非任何新定理的誕生。

---

## 既有結果出處（供查證「無新發現」之聲明）

- Turing, A. M. (1936). On Computable Numbers, with an Application to the Entscheidungsproblem.
- Specker, E. (1949). 可計算單調有界序列，其極限非可計算。
- Kleene, S. C. (1945). On the interpretation of intuitionistic number theory（可實現性）。
- Avizienis, A. (1961). Signed-digit number representations for fast parallel arithmetic.
- Bishop, E. (1967). Foundations of Constructive Analysis；Bishop & Bridges (1985). Constructive Analysis.
- Richardson, D. (1968). Some undecidable problems involving elementary functions of a real variable.
- Myhill, J. (1971). 一個可計算、處處可微、導數連續卻不可計算的函數。
- Pour-El, M. B. & Richards, J. I. (1989). Computability in Analysis and Physics.
- Weihrauch, K. (2000). Computable Analysis: An Introduction（TTE）。
- Cruz-Filipe, Geuvers & Wiedijk (2004). C-CoRN（Coq 構造實數）。
- Müller, N. iRRAM（exact real arithmetic 實作）。
- Lean mathlib：`Real`（Cauchy 完備化）、`DualNumber`（`TrivSqZeroExt`）。
- 前向模式自動微分與對偶數：Clifford (1873) 對偶數；Wengert (1964) 自動微分。
