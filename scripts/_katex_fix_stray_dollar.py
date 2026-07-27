#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""One-time repair script: inside row/column environments (cases, aligned,
align, array), some papers write literal currency amounts ("$10000", "$10^6",
"NT$10億") without escaping the dollar sign. Since the block is already in
math mode, marked-katex-extension and KaTeX both treat that bare $ as an
attempt to toggle math mode again -- KaTeX throws "Can't use function '$' in
math mode" (or, when the stray $ causes the renderer's own block-boundary
scan to misfire, cascades into unrelated "Unexpected end of input" errors on
ENTIRELY DIFFERENT blocks later in the same file).

Fix: escape any bare $ found strictly between a \begin{...} and its matching
\end{...} to \$. Scoped to cases/aligned/align/array specifically -- the same
scope already proven safe for the row-separator fix in
_katex_fix_cases_rowsep.py -- and NOT to $$...$$ generally: an earlier version
of this script scoped to raw $$...$$ and found a serious false positive. A
non-greedy $$...$$ scan can jump clean over a real closing $$ if, further
down the SAME file, two unrelated single-$ inline spans happen to sit back to
back with no space between them (closing $ of one span immediately followed
by the opening $ of the next) -- that accidental "$$" reads as a closer to
the regex, silently swallowing a huge stretch of legitimate standalone inline
math as if it were "inside" one giant broken block. Row/column environments
don't have that ambiguity: a real nested $ delimiter can never be legitimate
inside \begin{aligned}...\end{aligned} (nesting math mode inside math mode is
never valid LaTeX), so every bare $ found in that scope is unambiguously a
stray character that needs escaping, regardless of what precedes or follows it.

Usage: python scripts/_katex_fix_stray_dollar.py [--dry-run]
"""
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "content" / "papers"

CASES_RE = re.compile(r"\\begin\{(cases|aligned|align\*?|array)\}([\s\S]*?)\\end\{\1\}")
STRAY_DOLLAR_RE = re.compile(r"(?<!\\)\$")


def fix_block(inner: str) -> tuple[str, int]:
    return STRAY_DOLLAR_RE.subn(r"\\$", inner)


def fix_text(text: str) -> tuple[str, int]:
    count = 0

    def repl(m):
        nonlocal count
        env, inner = m.group(1), m.group(2)
        fixed, n = fix_block(inner)
        count += n
        return "\\begin{" + env + "}" + fixed + "\\end{" + env + "}"

    return CASES_RE.sub(repl, text), count


def main():
    dry = "--dry-run" in sys.argv
    files = sorted(p for p in PAPERS_DIR.rglob("*.md"))
    total_fixed_files = 0
    total_edits = 0
    log_path = Path("D:/tmp/stray_dollar_fix_report.txt")
    with io.open(log_path, "w", encoding="utf-8") as log:
        for f in files:
            text = f.read_text(encoding="utf-8")
            new_text, n = fix_text(text)
            if n:
                total_fixed_files += 1
                total_edits += n
                if not dry:
                    f.write_text(new_text, encoding="utf-8")
                log.write(f"{'[dry] ' if dry else ''}{f.relative_to(ROOT)}: {n} stray-$ fix(es)\n")
        log.write(f"\n{'[DRY RUN] ' if dry else ''}files touched: {total_fixed_files}, total edits: {total_edits}\n")
    print(f"done, see {log_path} -- files touched: {total_fixed_files}, total edits: {total_edits}")


if __name__ == "__main__":
    main()
