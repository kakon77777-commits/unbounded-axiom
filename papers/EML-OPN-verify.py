#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EML-OPN-v0.3  運算優先性的符號中立性猜想
完整展開系統實作與三層守恆驗證程式
EveMissLab | Theia  ·  2026年6月

對應論文附錄：
  A — 完整展開系統的形式化定義
  B 前置 — 解析歧義對照
  B、C   — 值守恆（同一樹在兩系統下的計算）
  D      — 代數路徑守恆（分配律）
"""

# ══════════════════════════════════════════════════════════════════
#  § 0  表達式樹（對應附錄 A.1）
# ══════════════════════════════════════════════════════════════════

class Node:
    """
    表達式樹節點。
    - 葉節點：op='val', value=整數
    - 內部節點：op='+' 或 '*', left/right=子節點
    """

    def __init__(self, op, left=None, right=None, value=None):
        self.op    = op
        self.left  = left
        self.right = right
        self.value = value

    def __repr__(self):
        if self.op == 'val':
            return str(self.value)
        return f"({self.left} {self.op} {self.right})"

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if self.op != other.op:
            return False
        if self.op == 'val':
            return self.value == other.value
        return self.left == other.left and self.right == other.right


def Val(n):     return Node('val', value=n)
def Add(l, r):  return Node('+', l, r)
def Mul(l, r):  return Node('*', l, r)


# ══════════════════════════════════════════════════════════════════
#  § 1  完整展開系統求值（對應附錄 A.2）
# ══════════════════════════════════════════════════════════════════

def fully_expanded_eval(tree, log=None, depth=0):
    """
    完整展開系統的遞迴求值。

    規則（對應附錄 A.2）：
    1. 加法：直接執行
    2. 乘法：以迴圈展開為重複加法
       由交換律取 min(a,b) 次、加 max(a,b) 的緊湊形式
    3. 每一步記入 log

    返回整數計算結果。
    """
    if log is None:
        log = []
    pad = "  " * depth

    # 葉節點
    if tree.op == 'val':
        log.append(f"{pad}葉  {tree.value}")
        return tree.value

    # 遞迴求左右子樹
    lv = fully_expanded_eval(tree.left,  log, depth + 1)
    rv = fully_expanded_eval(tree.right, log, depth + 1)

    if tree.op == '+':
        result = lv + rv
        log.append(f"{pad}ADD({lv}, {rv}) = {result}")
        return result

    # 乘法：完全展開為重複加法（不使用 Python 的 * 運算符）
    # 由交換律取較緊湊的展開方向
    if lv <= rv:
        times, addend = lv, rv
    else:
        times, addend = rv, lv

    expansion = " + ".join([str(addend)] * times)
    log.append(f"{pad}MUL({lv}, {rv})  →  {expansion}")

    result = 0
    for _ in range(times):
        result += addend

    log.append(f"{pad}MUL({lv}, {rv}) = {result}")
    return result


# ══════════════════════════════════════════════════════════════════
#  § 2  字串解析器（加法優先 S₊ 與乘法優先 S×）
# ══════════════════════════════════════════════════════════════════

def tokenize(s):
    """詞法分析：字串 → token 序列。接受 ASCII * 與 Unicode ×。"""
    tokens, i = [], 0
    while i < len(s):
        if s[i].isspace():
            i += 1
        elif s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            tokens.append(('NUM', int(s[i:j])))
            i = j
        elif s[i] in '+-()':
            tokens.append(('OP', s[i]))
            i += 1
        elif s[i] in '*×':
            tokens.append(('OP', '*'))
            i += 1
        else:
            i += 1
    return tokens


class _BaseParser:
    """解析器基底。"""

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos    = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def _primary(self):
        tok = self.peek()
        if tok and tok[0] == 'NUM':
            self.consume()
            return Val(tok[1])
        if tok and tok[1] == '(':
            self.consume()
            node = self._parse_expr()
            self.consume()          # 消耗 ')'
            return node
        raise SyntaxError(f"解析錯誤：位置 {self.pos}，token = {tok}")


class MulFirstParser(_BaseParser):
    """
    乘法優先系統 S×（標準 PEMDAS 約定）。

    文法（越內層優先順序越高）：
      expr     → add_expr
      add_expr → mul_expr ('+' mul_expr)*   ← '+' 外層：低優先
      mul_expr → primary  ('*' primary)*    ← '*' 內層：高優先
    """

    def _parse_expr(self):  return self._add_expr()

    def _add_expr(self):
        left = self._mul_expr()
        while self.peek() == ('OP', '+'):
            self.consume()
            left = Add(left, self._mul_expr())
        return left

    def _mul_expr(self):
        left = self._primary()
        while self.peek() == ('OP', '*'):
            self.consume()
            left = Mul(left, self._primary())
        return left

    def parse(self):
        return self._parse_expr()


class AddFirstParser(_BaseParser):
    """
    加法優先系統 S₊（反轉約定）。

    文法（越內層優先順序越高）：
      expr     → mul_expr
      mul_expr → add_expr ('*' add_expr)*   ← '*' 外層：低優先
      add_expr → primary  ('+' primary)*    ← '+' 內層：高優先
    """

    def _parse_expr(self):  return self._mul_expr()

    def _mul_expr(self):
        left = self._add_expr()
        while self.peek() == ('OP', '*'):
            self.consume()
            left = Mul(left, self._add_expr())
        return left

    def _add_expr(self):
        left = self._primary()
        while self.peek() == ('OP', '+'):
            self.consume()
            left = Add(left, self._primary())
        return left

    def parse(self):
        return self._parse_expr()


def parse_mf(s): return MulFirstParser(tokenize(s)).parse()
def parse_af(s): return AddFirstParser(tokenize(s)).parse()


# ══════════════════════════════════════════════════════════════════
#  § 3  驗證主程式
# ══════════════════════════════════════════════════════════════════

LINE  = "═" * 64
LINE2 = "─" * 54

def section(title):
    print(f"\n{LINE}\n  {title}\n{LINE}")


def run_verification():

    print(f"\n{'='*64}")
    print("  EML-OPN-v0.3  運算優先性的符號中立性猜想")
    print("  完整展開系統實作與三層守恆驗證")
    print("  EveMissLab | Theia  ·  2026年6月")
    print(f"{'='*64}")

    results = {}

    # ──────────────────────────────────────────────────────────────
    #  前置驗證：交換律等價性（對應附錄 A.2 的定義一致性）
    # ──────────────────────────────────────────────────────────────
    section("前置驗證：乘法展開的交換律等價性（附錄 A.2）")

    print("""
  附錄 A.2 定義：a × b := a + a + ... + a（b 次）
  由乘法交換律：a × b = b + b + ... + b（a 次）
  程式採用 min(a,b) 次、加 max(a,b) 的緊湊形式。
  以下驗證兩個方向結果相同。
    """)

    # 方向一：3 加 4 次（定義形式）
    r1, s1 = 0, []
    for _ in range(4):
        r1 += 3
        s1.append("3")
    print(f"  3 × 4  定義形式（3 加 4 次）：{' + '.join(s1)} = {r1}")

    # 方向二：4 加 3 次（交換律形式）
    r2, s2 = 0, []
    for _ in range(3):
        r2 += 4
        s2.append("4")
    print(f"  3 × 4  交換律形式（4 加 3 次）：{' + '.join(s2)} = {r2}")

    assert r1 == r2 == 12
    print(f"\n  ✓  兩個展開方向均得 {r1}，交換律等價性確認")
    results['pre'] = True

    # ──────────────────────────────────────────────────────────────
    #  第一層：約定守恆（附錄 B 前置）
    #  相同字串，不同系統 → 不同的樹 → 不同的值
    # ──────────────────────────────────────────────────────────────
    section("第一層：約定守恆——解析歧義對照（附錄 B 前置）")

    sigma = "2+3*4"
    T_af  = parse_af(sigma)
    T_mf  = parse_mf(sigma)

    assert T_af != T_mf

    print(f'\n  字串 σ = "{sigma}"\n')

    print(f"  S₊（加法優先）  →  樹 = {T_af}")
    log_af = []
    v_af = fully_expanded_eval(T_af, log_af)
    for s in log_af:
        print(f"      {s}")
    print(f"  S₊ 不動點 = {v_af}\n")

    print(f"  S×（乘法優先）  →  樹 = {T_mf}")
    log_mf = []
    v_mf = fully_expanded_eval(T_mf, log_mf)
    for s in log_mf:
        print(f"      {s}")
    print(f"  S× 不動點 = {v_mf}")

    assert v_af != v_mf
    print(f"\n  ✓  T_af ≠ T_mf（樹結構不同）")
    print(f"  ✓  {v_af} ≠ {v_mf}（不動點不同）")
    print(f"     → 約定決定字串被理解為哪個表達式樹")
    results['layer1'] = (v_af, v_mf)

    # ──────────────────────────────────────────────────────────────
    #  第二層：值守恆（附錄 B、C）
    #  同一棵樹，兩系統正確標記 → 解析後得到同一棵樹 → 狀態序列完全一致
    # ──────────────────────────────────────────────────────────────
    section("第二層：值守恆——同一樹在兩系統下的計算（附錄 B、C）")

    T         = Add(Val(2), Mul(Val(3), Val(4)))
    T_from_af = parse_af("2+(3*4)")     # S₊ 的正確標記
    T_from_mf = parse_mf("2+3*4")      # S× 的正確標記

    print(f"\n  數學意圖 T = ADD(2, MUL(3, 4)) = {T}")
    print(f"\n  S₊ 正確標記 \"2+(3×4)\"  →  解析結果: {T_from_af}")
    print(f"  S× 正確標記 \"2+3×4\"    →  解析結果: {T_from_mf}")

    assert T_from_af == T_from_mf == T
    print(f"  ✓  兩個標記解析後均得到同一棵樹 T")

    print(f"\n  {LINE2}")
    print(f"  附錄 B：S₊ 的完整展開")
    log_b = []
    v_b = fully_expanded_eval(T, log_b)
    for s in log_b:
        print(f"    {s}")
    print(f"  不動點: {v_b}")

    print(f"\n  {LINE2}")
    print(f"  附錄 C：S× 的完整展開")
    log_c = []
    v_c = fully_expanded_eval(T, log_c)
    for s in log_c:
        print(f"    {s}")
    print(f"  不動點: {v_c}")

    assert v_b == v_c == 14
    assert log_b == log_c
    print(f"\n  ✓  val(T) = {v_b}（兩系統一致）")
    print(f"  ✓  log_b == log_c：狀態序列逐步完全一致")
    print(f"     → 路徑未分叉，B 與 C 是同一條計算路徑（最強守恆形式）")
    results['layer2'] = v_b

    # ──────────────────────────────────────────────────────────────
    #  第三層：代數路徑守恆（附錄 D）
    #  兩棵結構不同的樹，由環公理保證，不動點相同
    # ──────────────────────────────────────────────────────────────
    section("第三層：代數路徑守恆——分配律匯流驗證（附錄 D）")

    a, b, c = 3, 4, 5
    T_L = Mul(Val(a), Add(Val(b), Val(c)))               # a(b+c)
    T_R = Add(Mul(Val(a), Val(b)), Mul(Val(a), Val(c)))  # ab+ac

    assert T_L != T_R       # 確認兩棵樹結構相異

    print(f"\n  a={a}, b={b}, c={c}")
    print(f"  T_L = {T_L}         （先加後乘：左側路徑）")
    print(f"  T_R = {T_R}  （先乘後加：右側路徑）")
    print(f"  ✓  T_L ≠ T_R（樹結構確認相異）")

    print(f"\n  {LINE2}")
    print(f"  左側路徑完整展開（先加後乘）:")
    log_L = []
    v_L = fully_expanded_eval(T_L, log_L)
    for s in log_L:
        print(f"    {s}")
    print(f"  不動點: {v_L}")

    print(f"\n  {LINE2}")
    print(f"  右側路徑完整展開（先乘後加）:")
    log_R = []
    v_R = fully_expanded_eval(T_R, log_R)
    for s in log_R:
        print(f"    {s}")
    print(f"  不動點: {v_R}")

    assert v_L == v_R == 27
    print(f"\n  ✓  val(T_L) = val(T_R) = {v_L}（不動點相同）")
    print(f"     → a(b+c) = ab+ac  ←→  匯流性的符號記錄")
    results['layer3'] = v_L

    # ──────────────────────────────────────────────────────────────
    #  總結
    # ──────────────────────────────────────────────────────────────
    section("驗證總結")

    print(f"""
  前置  乘法展開交換律等價性              通過  ✓
  ────────────────────────────────────────────────────
  第一層  約定守恆（解析歧義對照）
    σ = "2+3×4"
    S₊ 解析 → {T_af} = {v_af}
    S× 解析 → {T_mf} = {v_mf}
    同一字串，不同系統，結果相異          通過  ✓
  ────────────────────────────────────────────────────
  第二層  值守恆（同一樹，兩系統）
    T = {T}
    S₊ 展開 → {v_b}，S× 展開 → {v_c}
    狀態序列逐步完全一致                  通過  ✓
  ────────────────────────────────────────────────────
  第三層  代數路徑守恆（分配律）
    T_L = {T_L}，val = {v_L}
    T_R = {T_R}
    val = {v_R}
    樹結構相異，不動點相同                通過  ✓
  ────────────────────────────────────────────────────

  命題：運算優先順序是符號系統的投影補償協議；
        數學實在是匯流的，不動點存在且唯一。
    """)

    all_passed = (
        results['pre'] and
        results['layer1'] == (20, 14) and
        results['layer2'] == 14 and
        results['layer3'] == 27
    )

    print(f"  {'所有 assertion 通過，命題在本範例空間內未被反駁。' if all_passed else '驗證失敗。'}")
    return all_passed


if __name__ == "__main__":
    passed = run_verification()
    exit(0 if passed else 1)
