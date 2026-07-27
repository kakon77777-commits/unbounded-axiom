#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-time repair script (not part of the build pipeline): pads inline `$...$`
math spans that touch CJK/punctuation with no space, which is the single
largest KaTeX failure category found in the 2026-07-27 full-corpus sweep
("Can't use function '$' in math mode" — 1039 of 1699 errors). Same fix
already proven safe on many earlier batches (see project memory); this run
applies it retroactively to the older, never-swept part of the corpus.

Usage: python scripts/_katex_fix_dollar_adjacency.py [--dry-run]
"""
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "content" / "papers"

CJK_OR_PUNCT = "一-鿿、，。：；！？「」『』（）—…《》〈〉"
# A hyphen is deliberately its OWN, separate trigger set from CJK_OR_PUNCT,
# scoped to AFTER a closing $ only. "$C$-相對的" ("C"-relative, a hyphenated
# compound where C is a math variable) needs the same space fix — but a
# hyphen BEFORE an opening $ is left alone in the general case, since "-$5"
# could in principle be a negative number touching a NEW math span rather
# than a compound-word connector, and there's no such compound-word reading
# starting a fresh span the way there is right after a close.
AFTER_TRIGGERS = CJK_OR_PUNCT + "\\-"
# closing "$...$" immediately followed by CJK/punct/hyphen, no space. Both $
# are explicitly required to NOT be part of a $$ pair (negative lookbehind
# before the open, negative lookahead after the close) — otherwise a
# `$$...$$文字` display block with no space before the CJK could get misread
# as starting a NEW inline span at its second $, one character in the wrong place.
AFTER_CLOSE_RE = re.compile(r"(?<!\$)\$([^\$\n]{1,80}?)\$(?!\$)(?=[" + AFTER_TRIGGERS + r"])")
# CJK/punct immediately followed by an opening "$", no space
BEFORE_OPEN_RE = re.compile(r"([" + CJK_OR_PUNCT + r"])\$(?!\$)")

# Genuine inline math is short and math-shaped. A misfired match spanning
# ordinary prose (e.g. because it landed on a $$ boundary in an unanticipated
# way) would tend to be longer and have none of these — an extra guard on
# top of the $$ lookaround above, not a replacement for it.
_MATHY_RE = re.compile(r"[\\^_{}=<>+\-\d]")


def _looks_like_math(s: str) -> bool:
    return len(s) <= 40 or bool(_MATHY_RE.search(s))


def fix_text(text: str) -> tuple[str, int]:
    count = 0

    def after_close(m):
        nonlocal count
        if not _looks_like_math(m.group(1)):
            return m.group(0)
        count += 1
        return "$" + m.group(1) + "$ "

    text = AFTER_CLOSE_RE.sub(after_close, text)

    def before_open(m):
        nonlocal count
        count += 1
        return m.group(1) + " $"

    text = BEFORE_OPEN_RE.sub(before_open, text)
    return text, count


def main():
    dry = "--dry-run" in sys.argv
    files = sorted(p for p in PAPERS_DIR.rglob("*.md"))
    total_fixed_files = 0
    total_edits = 0
    log_path = Path("D:/tmp/dollar_fix_report.txt")
    with io.open(log_path, "w", encoding="utf-8") as log:
        for f in files:
            text = f.read_text(encoding="utf-8")
            new_text, n = fix_text(text)
            if n:
                total_fixed_files += 1
                total_edits += n
                if not dry:
                    f.write_text(new_text, encoding="utf-8")
                log.write(f"{'[dry] ' if dry else ''}{f.relative_to(ROOT)}: {n} spacing fix(es)\n")
        log.write(f"\n{'[DRY RUN] ' if dry else ''}files touched: {total_fixed_files}, total edits: {total_edits}\n")
    print(f"done, see {log_path} — files touched: {total_fixed_files}, total edits: {total_edits}")


if __name__ == "__main__":
    main()
