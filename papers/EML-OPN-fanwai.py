#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EML-OPN 番外篇
純中文數字系統（算籌）× 幾何語言表示論（弦圖 / Cl(2,0) / 矩陣）
EML-OPN-fanwai.py
EveMissLab | Theia · 2026年6月

驗證兩項延伸命題：
  甲  相同的三層守恆結構，在純中文數字 / 算籌系統中完整成立
  乙  勾股定理（幾何真值）在三種表示語言下擁有同一不動點，
      表示論是不同幾何語言之間等價性的保證機制
"""

# ══════════════════════════════════════════════════════════════════
#  A  中文數字工具
# ══════════════════════════════════════════════════════════════════

DIGITS = '零一二三四五六七八九'

def to_cn(n):
    """非負整數 → 中文數字串。"""
    if n < 10:  return DIGITS[n]
    if n < 20:  return '十' + (DIGITS[n % 10] if n % 10 else '')
    if n < 100:
        t, o = n // 10, n % 10
        return DIGITS[t] + '十' + (DIGITS[o] if o else '')
    if n < 1000:
        h, rest = n // 100, n % 100
        if rest == 0:   return DIGITS[h] + '百'
        if rest < 10:   return DIGITS[h] + '百零' + DIGITS[rest]
        return DIGITS[h] + '百' + to_cn(rest)
    return str(n)   # 超出範圍時回退 Arabic

# ══════════════════════════════════════════════════════════════════
#  B  表達式樹（與主程式完全相同，重新定義以避免導入問題）
# ══════════════════════════════════════════════════════════════════

class Node:
    def __init__(self, op, left=None, right=None, value=None):
        self.op, self.left, self.right, self.value = op, left, right, value
    def __repr__(self):
        if self.op == 'val': return str(self.value)
        return f"({self.left} {self.op} {self.right})"
    def __eq__(self, other):
        if not isinstance(other, Node) or self.op != other.op: return False
        if self.op == 'val': return self.value == other.value
        return self.left == other.left and self.right == other.right

def Val(n):    return Node('val', value=n)
def Add(l, r): return Node('+', l, r)
def Mul(l, r): return Node('*', l, r)

# ══════════════════════════════════════════════════════════════════
#  C  算籌求值器
#  邏輯與主程式 fully_expanded_eval 完全相同；
#  差異僅在顯示層：數值以中文呈現，術語取自古算語彙。
#  此函數的存在本身即第一直接證據：
#  符號系統（中文 ↔ 阿拉伯）的替換不改變計算結構。
# ══════════════════════════════════════════════════════════════════

def suanpan_eval(tree, log=None, depth=0):
    if log is None: log = []
    pad = '  ' * depth

    if tree.op == 'val':
        log.append(f"{pad}末算  {to_cn(tree.value)}")
        return tree.value

    lv = suanpan_eval(tree.left,  log, depth + 1)
    rv = suanpan_eval(tree.right, log, depth + 1)

    if tree.op == '+':
        r = lv + rv
        log.append(f"{pad}以{to_cn(lv)}加{to_cn(rv)}，得{to_cn(r)}")
        return r

    # 乘法 → 重複加法（算籌逐次累加）
    times, addend = (lv, rv) if lv <= rv else (rv, lv)
    marks = '＋'.join([to_cn(addend)] * times)
    log.append(f"{pad}以{to_cn(addend)}累加{to_cn(times)}次（{marks}）")
    r = 0
    for _ in range(times): r += addend
    log.append(f"{pad}乘得{to_cn(r)}")
    return r

# ══════════════════════════════════════════════════════════════════
#  D  幾何代數 Cl(2,0)
#  基底：{1, e₁, e₂, e₁₂}，分量記為 (s, v1, v2, b)
#  乘法規則：e₁²=1  e₂²=1  e₁e₂=e₁₂  e₂e₁=−e₁₂  e₁₂²=−1
# ══════════════════════════════════════════════════════════════════

class Cl2:
    def __init__(self, s=0., v1=0., v2=0., b=0.):
        self.s, self.v1, self.v2, self.b = float(s), float(v1), float(v2), float(b)

    @classmethod
    def vec(cls, a, b): return cls(0, a, b, 0)

    def __add__(self, o):
        return Cl2(self.s+o.s, self.v1+o.v1, self.v2+o.v2, self.b+o.b)

    def __mul__(self, o):
        # 完整 Cl(2,0) 幾何積，基底乘法表展開
        a, b = self, o
        return Cl2(
            a.s*b.s  + a.v1*b.v1 + a.v2*b.v2 - a.b*b.b,   # scalar
            a.s*b.v1 + a.v1*b.s  - a.v2*b.b  + a.b*b.v2,   # e₁
            a.s*b.v2 + a.v1*b.b  + a.v2*b.s  - a.b*b.v1,   # e₂
            a.s*b.b  + a.v1*b.v2 - a.v2*b.v1 + a.b*b.s     # e₁₂
        )

    def norm_sq(self):
        """向量範數平方 = v1²+v2²（grade-1 向量自乘之純量部分）"""
        return (self * self).s

    def __repr__(self):
        t = []
        for v, name in [(self.s,''), (self.v1,'e₁'), (self.v2,'e₂'), (self.b,'e₁₂')]:
            if abs(v) > 1e-10: t.append(f"{v:g}{name}")
        return ' + '.join(t) or '0'

# ══════════════════════════════════════════════════════════════════
#  E  矩陣表示（Cl(2,0) 的 2×2 實矩陣同構）
#  e₁ ↦ [[1,0],[0,−1]]   e₂ ↦ [[0,1],[1,0]]   e₁₂ ↦ [[0,1],[−1,0]]
#  向量 ae₁+be₂ ↦ [[a,b],[b,−a]]
#  表示論保證：Cl(2,0) 中成立的等式，在此表示下也成立
# ══════════════════════════════════════════════════════════════════

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def mat_add(A, B):
    return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]

def vec_to_mat(a, b):
    """向量 ae₁ + be₂ → 矩陣表示"""
    return [[a, b], [b, -a]]

def mat_norm_sq(M):
    """‖v‖² = trace(M²)/2（對 grade-1 向量的矩陣表示成立）"""
    M2 = mat_mul(M, M)
    return (M2[0][0] + M2[1][1]) / 2

# ══════════════════════════════════════════════════════════════════
#  F  弦圖面積計算（出入相補原理，純加法）
#  外正方形面積 = 四三角形合計 + 中央小正方形
#  弦² = 2×gou×gu + (gu−gou)² = gou² + gu²
# ══════════════════════════════════════════════════════════════════

def xian_tu(gou, gu):
    """
    以純加法實現弦圖的面積計算。
    返回 (弦², 四三角形合計面積, 中央正方形面積, 中央正方形邊長)
    """
    # 四個三角形面積總和 = 4×gou×gu（純加法）
    four_gou_gu = 0
    for _ in range(4):
        for _ in range(gou):
            four_gou_gu += gu
    two_gou_gu = four_gou_gu // 2   # = 2×gou×gu

    # 中央小正方形邊長 = |gu - gou|，面積（純加法）
    side = abs(gu - gou)
    inner = 0
    for _ in range(side): inner += side

    return two_gou_gu + inner, two_gou_gu, inner, side

# ══════════════════════════════════════════════════════════════════
#  主驗證
# ══════════════════════════════════════════════════════════════════

LINE  = '═' * 64
LINE2 = '─' * 52

def section(title):
    print(f"\n{LINE}\n  {title}\n{LINE}")

def run():
    print(f"\n{'='*64}")
    print("  EML-OPN 番外篇")
    print("  純中文數字（算籌） × 幾何語言表示論（弦圖/Cl(2,0)/矩陣）")
    print("  EveMissLab | Theia  ·  2026年6月")
    print(f"{'='*64}")

    results = {}

    # ──────────────────────────────────────────────────────────────
    #  番外甲：算籌系統三層守恆
    # ──────────────────────────────────────────────────────────────
    section("番外甲：算籌系統（中文數字顯示）——三層守恆")

    # ── 甲-一：第一層（約定守恆 / 語言歧義）────────────────────
    print(f"""
  【甲-一】語言歧義對照（對應附錄 B 前置）

  字串：「二加三乘四」

  讀法一（中文從左至右自然閱讀，等同加法優先 S₊）：
    （二加三）乘四

  讀法二（古算顯式語序，等同乘法優先 S×）：
    以三乘四得十二，再加二

  古典算書（如《九章算術》）採顯式語序避免歧義，
  即：自然語言的古算表達傾向完整展開系統。
    """)

    T_read1 = Mul(Add(Val(2), Val(3)), Val(4))   # 讀法一的樹
    T_read2 = Add(Val(2), Mul(Val(3), Val(4)))   # 讀法二的樹

    log1, log2 = [], []
    v1 = suanpan_eval(T_read1, log1)
    v2 = suanpan_eval(T_read2, log2)

    print("  讀法一（加法優先）的算籌步驟：")
    for s in log1: print(f"    {s}")
    print(f"  不動點：{to_cn(v1)}（{v1}）\n")

    print("  讀法二（乘法優先）的算籌步驟：")
    for s in log2: print(f"    {s}")
    print(f"  不動點：{to_cn(v2)}（{v2}）")

    assert v1 == 20 and v2 == 14
    print(f"\n  ✓  {to_cn(v1)}（{v1}） ≠ {to_cn(v2)}（{v2}）")
    print(f"     → 約定決定語義，此層守恆為前提層")
    results['cn_layer1'] = (v1, v2)

    # ── 甲-二：第二層（值守恆）──────────────────────────────────
    print(f"\n  {LINE2}")
    print("  【甲-二】值守恆（對應附錄 B、C）")

    T = Add(Val(2), Mul(Val(3), Val(4)))
    la, lb = [], []
    va = suanpan_eval(T, la)
    vb = suanpan_eval(T, lb)

    assert va == vb == 14
    assert la == lb

    print(f"  確定意圖為讀法二（以三乘四得十二，加以二）")
    for s in la: print(f"    {s}")
    print(f"  算籌步驟序列唯一，不動點：{to_cn(va)}（{va}）")
    print(f"  ✓  兩次計算步驟逐條完全一致（log_a == log_b）")
    print(f"     中文數字系統值守恆通過")
    results['cn_layer2'] = va

    # ── 甲-三：第三層（代數路徑守恆 / 交換律）───────────────────
    print(f"\n  {LINE2}")
    print("  【甲-三】代數路徑守恆（乘法兩種展開路徑）")

    # 路徑甲：以四累加三次（三×四，按定義方向：三出現四次）
    path_a = 0
    steps_a = []
    for _ in range(4):
        path_a += 3
        steps_a.append(to_cn(3))
    # 路徑乙：以三累加四次（四×三，交換律等價形式：四出現三次）
    path_b = 0
    steps_b = []
    for _ in range(3):
        path_b += 4
        steps_b.append(to_cn(4))

    print(f"  路徑甲（以三累加四次）：{'＋'.join(steps_a)} = {to_cn(path_a)}")
    print(f"  路徑乙（以四累加三次）：{'＋'.join(steps_b)} = {to_cn(path_b)}")
    assert path_a == path_b == 12
    print(f"  ✓  兩條路徑均得{to_cn(path_a)}（{path_a}），代數路徑守恆通過")
    results['cn_layer3'] = path_a

    # ──────────────────────────────────────────────────────────────
    #  番外乙：勾股定理三重表示
    # ──────────────────────────────────────────────────────────────
    section("番外乙：幾何語言表示論——勾股定理三重表示")

    gou, gu = 3, 4
    xian_sq_expected = gou**2 + gu**2  # = 25

    print(f"\n  勾 = {to_cn(gou)}，股 = {to_cn(gu)}")
    print(f"  驗證命題：弦² = 勾² + 股² = {to_cn(gou)}² + {to_cn(gu)}² = {to_cn(xian_sq_expected)}")
    print(f"\n  三種表示語言分別獨立計算，確認不動點一致。")

    # ── 乙-一：弦圖（幾何語言，出入相補）────────────────────────
    print(f"\n  {LINE2}")
    print("  【表示一】弦圖（出入相補原理，純加法）")

    xian_sq_geo, two_gou_gu, inner_area, side_inner = xian_tu(gou, gu)

    print(f"  以四個勾{to_cn(gou)}股{to_cn(gu)}的直角三角形圍成外正方形：")
    print(f"  四個三角形合計面積 = 四×勾×股÷二")
    print(f"    = 四×{to_cn(gou)}×{to_cn(gu)}÷二（純加法計算）= {to_cn(two_gou_gu)}")
    print(f"  中央小正方形邊長 = |股−勾| = |{to_cn(gu)}−{to_cn(gou)}| = {to_cn(side_inner)}")
    print(f"  中央小正方形面積 = {to_cn(side_inner)}² = {to_cn(inner_area)}")
    print(f"  弦² = {to_cn(two_gou_gu)} + {to_cn(inner_area)} = {to_cn(xian_sq_geo)}")
    assert xian_sq_geo == xian_sq_expected
    print(f"  ✓  弦圖語言得弦² = {to_cn(xian_sq_geo)}（{xian_sq_geo}）")
    results['geo_xiantu'] = xian_sq_geo

    # ── 乙-二：幾何代數 Cl(2,0)────────────────────────────────
    print(f"\n  {LINE2}")
    print("  【表示二】幾何代數 Cl(2,0)")
    print(f"  基底 {{1, e₁, e₂, e₁₂}}，規則：e₁²=e₂²=1，e₁₂²=−1，e₁e₂=−e₂e₁=e₁₂")

    a = Cl2.vec(gou, 0)    # 勾向量 = gou·e₁
    b = Cl2.vec(0, gu)     # 股向量 = gu·e₂（與 a 垂直）
    c = a + b              # 弦向量

    ab = a * b
    ba = b * a
    inner_ab = (ab.s + ba.s) / 2   # 內積 = (ab+ba)/2 的純量部分

    print(f"\n  a（勾向量）= {a}  →  a·a = {a.norm_sq():.0f}")
    print(f"  b（股向量）= {b}  →  b·b = {b.norm_sq():.0f}")
    print(f"  a×b = {ab}  （幾何積）")
    print(f"  b×a = {ba}  （幾何積）")
    print(f"  內積 a·b = (ab+ba)/2 的純量部分 = {inner_ab:.0f}  ← 垂直確認")
    print(f"  c（弦向量）= a+b = {c}")

    c_sq = c.norm_sq()
    print(f"  c·c（幾何積純量部分）= {c_sq:.0f}")

    assert abs(inner_ab) < 1e-9, "垂直條件失敗"
    assert abs(c_sq - xian_sq_expected) < 1e-9
    print(f"  ✓  Cl(2,0) 語言得弦² = {c_sq:.0f}")
    results['geo_cl2'] = c_sq

    # ── 乙-三：矩陣表示（表示論投影）────────────────────────────
    print(f"\n  {LINE2}")
    print("  【表示三】矩陣表示（Cl(2,0) 的 2×2 實矩陣同構）")
    print(f"  表示論保證：Cl(2,0) 中成立的等式，在所有忠實表示中均成立")

    Ma = vec_to_mat(gou, 0)
    Mb = vec_to_mat(0, gu)
    Mc = mat_add(Ma, Mb)

    nsa = mat_norm_sq(Ma)
    nsb = mat_norm_sq(Mb)
    nsc = mat_norm_sq(Mc)

    print(f"\n  M(a) = [[{Ma[0][0]}, {Ma[0][1]}], [{Ma[1][0]}, {Ma[1][1]}]]")
    print(f"  M(b) = [[{Mb[0][0]}, {Mb[0][1]}], [{Mb[1][0]}, {Mb[1][1]}]]")
    print(f"  M(c) = M(a)+M(b) = [[{Mc[0][0]}, {Mc[0][1]}], [{Mc[1][0]}, {Mc[1][1]}]]")
    print(f"  ‖a‖² = trace(M(a)²)/2 = {nsa:.0f}")
    print(f"  ‖b‖² = trace(M(b)²)/2 = {nsb:.0f}")
    print(f"  ‖c‖² = trace(M(c)²)/2 = {nsc:.0f}")

    assert abs(nsc - xian_sq_expected) < 1e-9
    print(f"  ✓  矩陣語言得弦² = {nsc:.0f}")
    results['geo_mat'] = nsc

    # ── 三重不動點匯流確認 ────────────────────────────────────────
    print(f"\n  {LINE2}")
    print("  三重表示不動點對照")
    print(f"  弦圖（幾何語言）         弦² = {xian_sq_geo}")
    print(f"  幾何代數 Cl(2,0)         弦² = {int(c_sq)}")
    print(f"  矩陣表示（表示論投影）   弦² = {int(nsc)}")

    assert xian_sq_geo == int(c_sq) == int(nsc) == xian_sq_expected
    print(f"\n  ✓  三種語言，同一不動點：{to_cn(xian_sq_expected)}（{xian_sq_expected}）")
    print(f"     {to_cn(gou)}² + {to_cn(gu)}² = {to_cn(gou**2)} + {to_cn(gu**2)} = {to_cn(xian_sq_expected)} = 弦²")

    # ──────────────────────────────────────────────────────────────
    #  總結
    # ──────────────────────────────────────────────────────────────
    section("番外篇驗證總結")

    print(f"""
  番外甲（算籌 / 中文數字系統）
  ──────────────────────────────────────────────────────
  甲-一  語言歧義對照
         讀法一 →（二加三）乘四 = {to_cn(results['cn_layer1'][0])}
         讀法二 → 以三乘四得十二加二 = {to_cn(results['cn_layer1'][1])}
         不同意圖，不同不動點                    通過  ✓
  甲-二  值守恆
         確定意圖後，算籌步驟序列唯一
         不動點 = {to_cn(results['cn_layer2'])}
         log_a == log_b，路徑未分叉              通過  ✓
  甲-三  代數路徑守恆（乘法交換律）
         兩種展開路徑均得{to_cn(results['cn_layer3'])}              通過  ✓

  番外乙（幾何語言表示論）
  ──────────────────────────────────────────────────────
  勾 = {to_cn(gou)}，股 = {to_cn(gu)}，預期弦² = {to_cn(xian_sq_expected)}

  弦圖（幾何語言 / 出入相補）  弦² = {to_cn(results['geo_xiantu'])}          通過  ✓
  幾何代數 Cl(2,0)              弦² = {to_cn(int(results['geo_cl2']))}          通過  ✓
  矩陣表示（表示論投影）        弦² = {to_cn(int(results['geo_mat']))}          通過  ✓
  三種語言，同一不動點           = {to_cn(xian_sq_expected)}              通過  ✓
  ──────────────────────────────────────────────────────

  命題延伸：
  不僅算術真值，幾何真值同樣是表示系統選擇下的不動點。
  表示論（Representation Theory）是形式化地保證
  「不同語言描述同一數學對象」的機制。
  符號語言（算籌、坐標、Clifford 代數、矩陣）各有投影的邊界，
  而它們所指向的實在，在所有邊界之外，自行存在。
    """)

    return True

if __name__ == '__main__':
    success = run()
    exit(0 if success else 1)
