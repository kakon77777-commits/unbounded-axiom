#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""One-time repair script: escapes bare `_` inside `\text{...}` (and the other
common text-mode wrappers) to `\_`. KaTeX's text mode does not treat `_` as
subscript, but its MATH-MODE tokenizer still sees the underscore before it
even reaches text mode content in some malformed inputs, producing "Expected
'EOF', got '_'" — the second-largest category in the 2026-07-27 full-corpus
sweep (90 of 1699 errors). Same fix pattern used on several earlier batches.

Usage: python scripts/_katex_fix_text_underscore.py [--dry-run]
"""
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "content" / "papers"

# \text{...}, \textbf{...}, \textrm{...}, \mathrm{...} — the content between
# the braces is text-mode-ish (or at least never subscript-bearing), so any
# bare underscore in there is almost certainly a literal underscore that
# needs escaping, not an intended subscript operator.
WRAPPER_RE = re.compile(r"\\(text|textbf|textrm|textit|mathrm)\{([^{}]*)\}")
BARE_UNDERSCORE_RE = re.compile(r"(?<!\\)_")
# A \text{...} block can itself drop back into math mode via a nested $...$
# (e.g. "\text{$f_0$／有聲狀態路徑}") — the underscore in f_0 there is a real
# subscript, not a literal one, and escaping it breaks the render the OTHER
# way. Split on $-delimited segments first; only touch the segments outside
# any $...$ pair.
DOLLAR_SPLIT_RE = re.compile(r"(\$[^\$]*\$)")


def _fix_plain_segment(segment: str) -> tuple[str, int]:
    return BARE_UNDERSCORE_RE.subn(r"\\_", segment)


def fix_text(text: str) -> tuple[str, int]:
    count = 0

    def fix_wrapper(m):
        nonlocal count
        cmd, inner = m.group(1), m.group(2)
        parts = DOLLAR_SPLIT_RE.split(inner)
        new_parts = []
        for i, part in enumerate(parts):
            if i % 2 == 1:  # odd indices are the $...$ segments — leave untouched
                new_parts.append(part)
            else:
                fixed, n = _fix_plain_segment(part)
                count += n
                new_parts.append(fixed)
        return f"\\{cmd}{{{''.join(new_parts)}}}"

    return WRAPPER_RE.sub(fix_wrapper, text), count


def main():
    dry = "--dry-run" in sys.argv
    files = sorted(p for p in PAPERS_DIR.rglob("*.md"))
    total_fixed_files = 0
    total_edits = 0
    log_path = Path("D:/tmp/underscore_fix_report.txt")
    with io.open(log_path, "w", encoding="utf-8") as log:
        for f in files:
            text = f.read_text(encoding="utf-8")
            new_text, n = fix_text(text)
            if n:
                total_fixed_files += 1
                total_edits += n
                if not dry:
                    f.write_text(new_text, encoding="utf-8")
                log.write(f"{'[dry] ' if dry else ''}{f.relative_to(ROOT)}: {n} underscore fix(es)\n")
        log.write(f"\n{'[DRY RUN] ' if dry else ''}files touched: {total_fixed_files}, total edits: {total_edits}\n")
    print(f"done, see {log_path} — files touched: {total_fixed_files}, total edits: {total_edits}")


if __name__ == "__main__":
    main()
