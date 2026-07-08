#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auto-repair Canvas copy-paste math corruption during §25 ingest.

Context: GPT/Canvas authors math with \\[…\\] (display) and \\(…\\) (inline). The
site renders those natively (see shell/src/lib/md.ts), so a CLEAN "download" export
needs NO change and is left byte-for-byte faithful. But "copy-paste from the Canvas
*rendered* view" scrapes the DOM and mangles structure — \\[ opens but a bare ] closes,
<br>→trailing \\, _→\\_, }_{→}*{, ]→$$, formulas→'# heading'/'----' rules, inline math
→ bare (…). is_corrupted() detects that signature; only then do we normalize (to $$,
which the site also renders). The transform is MATH-SPAN-AWARE: inline conversion runs
only in prose, never inside a math span, so literal function-application parens f(x)
inside a display block stay literal.

Used by scripts/ingest.py (Stage 1). Standalone: python scripts/normalize_math.py <dir>
"""
import io
import re
import sys
from pathlib import Path

MATH_SPAN = re.compile(r"\$\$.*?\$\$|\$[^$\n]+?\$", re.S)
CJK = re.compile(r"[一-鿿぀-ヿ]")
# CJK ideographs + kana + CJK/fullwidth punctuation + dashes/ellipsis/quotes: an inline
# $ touching any of these is NOT recognized as a delimiter under nonStandard:false, so
# we pad it with an ASCII space (the reliable fix short of flipping the global config).
CJK_ADJ = re.compile(r"[　-〿㐀-鿿＀-￯—–…‘’“”]")


def is_corrupted(t: str) -> bool:
    """True if the text shows copy-paste-from-rendered-view mangling (not a clean
    \\[…\\] download and not $$-native)."""
    if "\\[\\" in t or "*{" in t:                     # \[ + stray \  ;  }_{ -> }*{
        return True
    lone_close = len(re.findall(r"(?m)^\s*\]\s*$", t))  # bare ] on its own line = mangled close
    esc_close = len(re.findall(r"\\\]", t))
    if lone_close >= 3 and lone_close > esc_close:      # closes with bare ] far more than \]
        return True
    if len(re.findall(r"(?m)[^\\]\\\s*$", t)) >= 6:     # many <br>→ lone trailing \
        return True
    return False


def convert(t: str) -> str:
    """Normalize mangled bracket/paren math to $$/$ (site-renderable)."""
    # 1. DISPLAY delimiters, line-based, STATEFUL: a \[-line opens; the NEXT lone \]/]-
    #    line closes. Other lone ]-lines (arrays, lists, literal) stay put.
    out, in_disp = [], False
    for ln in t.split("\n"):
        if not in_disp and re.match(r"^\s*>?\s*\\\[\\?\s*$", ln):
            out.append(re.sub(r"\\\[\\?", "$$", ln)); in_disp = True; continue
        if in_disp and re.match(r"^\s*>?\s*(\\\]|\])\s*$", ln):
            out.append(re.sub(r"(\\\]|\])", "$$", ln)); in_disp = False; continue
        out.append(ln)
    t = "\n".join(out)

    # 2. inline \(...\) -> $...$
    t = t.replace("\\(", "$").replace("\\)", "$")

    # 3. Variant-B bare-paren inline -> $...$, ONLY in prose (outside existing math spans)
    def bare_paren(seg):
        return re.sub(
            r"\(([^()\n]{1,120})\)",
            lambda m: "$" + m.group(1) + "$" if ("\\" in m.group(1) and not CJK.search(m.group(1))) else m.group(0),
            seg)
    res, last = [], 0
    for mm in MATH_SPAN.finditer(t):
        res.append(bare_paren(t[last:mm.start()]))
        res.append(mm.group(0))
        last = mm.end()
    res.append(bare_paren(t[last:]))
    t = "".join(res)

    # 4. inside ALL math spans: \_->_, literal \[->[ \]->], strip lone trailing \, and
    #    neutralize markdown artifacts the exporter mangled INTO math (# headings, ---- rules)
    def fixmath(m):
        s = m.group(0)
        s = s.replace("\\_", "_").replace("\\[", "[").replace("\\]", "]")
        s = re.sub(r"(?<!\\)\\(\s*\r?\n)", r"\1", s)
        s = re.sub(r"(?m)^\s*[-=]{3,}\s*$", "", s)
        s = re.sub(r"(?m)^(\s*)#{1,6}[ \t]+", r"\1", s)
        return s
    t = MATH_SPAN.sub(fixmath, t)

    # 5. space-pad inline $...$ hugging CJK (see pad_inline_cjk)
    return pad_inline_cjk(t)


def pad_inline_cjk(t: str) -> str:
    """Space-pad inline $...$ that hug CJK/punct so nonStandard:false recognizes the
    delimiters. No-op on a clean \\[…\\] download (it has \\(…\\), not $), so it is safe
    to run on every paper and keeps faithful downloads byte-for-byte identical."""
    def pad_prose(seg):
        o, last = [], 0
        for mm in re.finditer(r"\$[^$\n]+?\$", seg):
            o.append(seg[last:mm.start()])
            left = seg[mm.start() - 1] if mm.start() > 0 else " "
            right = seg[mm.end()] if mm.end() < len(seg) else " "
            o.append((" " if CJK_ADJ.match(left) else "") + mm.group(0) + (" " if CJK_ADJ.match(right) else ""))
            last = mm.end()
        o.append(seg[last:])
        return "".join(o)
    res, last = [], 0
    for mm in re.finditer(r"\$\$.*?\$\$", t, re.S):
        res.append(pad_prose(t[last:mm.start()])); res.append(mm.group(0)); last = mm.end()
    res.append(pad_prose(t[last:]))
    return "".join(res)


def normalize(t: str) -> str:
    """Repair copy-paste corruption (only if detected); otherwise just CJK-pad inline
    $ (a no-op on clean \\[…\\] downloads). Faithful to clean downloads, fixes the rest."""
    return convert(t) if is_corrupted(t) else pad_inline_cjk(t)


if __name__ == "__main__":
    d = Path(sys.argv[1])
    for p in sorted(d.rglob("*.md")):
        raw = io.open(p, encoding="utf-8", newline="").read()
        new = normalize(raw)
        if new != raw:
            io.open(p, "w", encoding="utf-8", newline="").write(new)
            print(f"[normalize] repaired {p.name}")
        else:
            print(f"[normalize] clean, untouched: {p.name}")
