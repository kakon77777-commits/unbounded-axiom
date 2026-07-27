#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""One-time repair script: within math spans ($$...$$ and $...$), halves a
DOUBLED command backslash (`\\text` -> `\text`, `\\begin` -> `\begin`) back to
a single one. This is the same "batch-6" escape-corruption family documented
in project memory (some upstream generation/copy step doubled every command
backslash) — this run found it recurring in older (pre-2026-07) papers that
were never swept for it.

The one thing this must NOT touch: a standalone `\\` is genuine, correct
LaTeX for "start a new row" inside aligned/array/cases environments — that is
ALSO two backslash characters, but it is not "a doubled command backslash",
it is a real command in its own right. The distinguishing signal: a doubled
COMMAND backslash is always followed by a letter (`\\text`, `\\begin`,
`\\quad` — `\\` + [a-zA-Z]); a genuine row-separator `\\` is followed by
whitespace, `&`, or another `\`, never directly by a letter. Only the first
pattern is touched here.

Usage: python scripts/_katex_fix_doubled_backslash.py [--dry-run]
"""
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "content" / "papers"

MATH_SPAN_RE = re.compile(r"\$\$([\s\S]*?)\$\$|\$([^\$\n]+?)\$")
DOUBLED_CMD_RE = re.compile(r"\\\\(?=[A-Za-z])")

# Only touch a span if it shows the doubling pattern on a KNOWN, common LaTeX
# command name — guards against a false trigger on some unrelated `\\X` that
# isn't actually this corruption (e.g. `\\` immediately before a single
# stray letter that isn't really a command, if that ever occurs).
KNOWN_DOUBLED_CMDS_RE = re.compile(
    r"\\\\(text|textbf|textrm|textit|boxed|begin|end|quad|qquad|downarrow|uparrow|"
    r"rightarrow|Rightarrow|leftarrow|sum|frac|mathcal|mathbb|mathrm|cdot|in|leq|geq|"
    r"times|infty|partial|nabla|alpha|beta|gamma|delta|epsilon|theta|lambda|mu|sigma|"
    r"phi|psi|omega|pi|rho|tau|to|forall|exists|neq|approx|equiv|subset|supset|cup|cap)\b"
)

# Sibling bug found in the same corrupted files: the row-separator `\\` (a
# genuine, correct 2-backslash LaTeX command in its own right — see module
# docstring) sometimes ALSO got doubled by the same corruption event, to 4
# backslashes. Exactly 4, not followed by a letter (that would be a doubled
# command backslash butted up against this, handled separately above).
DOUBLED_LINEBREAK_RE = re.compile(r"\\\\\\\\(?![A-Za-z])")


def fix_span(inner: str) -> tuple[str, int]:
    count = 0
    if KNOWN_DOUBLED_CMDS_RE.search(inner):
        inner, n = DOUBLED_CMD_RE.subn(r"\\", inner)
        count += n
    if "\\\\\\\\" in inner:
        inner, n = DOUBLED_LINEBREAK_RE.subn(r"\\\\", inner)
        count += n
    return inner, count


def fix_text(text: str) -> tuple[str, int]:
    count = 0

    def repl(m):
        nonlocal count
        display, inline = m.group(1), m.group(2)
        if display is not None:
            fixed, n = fix_span(display)
            count += n
            return "$$" + fixed + "$$"
        else:
            fixed, n = fix_span(inline)
            count += n
            return "$" + fixed + "$"

    return MATH_SPAN_RE.sub(repl, text), count


def fix_text_to_fixed_point(text: str, max_passes: int = 5) -> tuple[str, int]:
    """A few files got their backslashes doubled TWICE (quadruple, not just
    double) — one pass of fix_text only halves 4 backslashes to 3, not to 1
    (the regex matches non-overlapping pairs left to right, so on `\\\\\\\\text`
    it fixes the LAST pair before the letter and leaves the first pair alone).
    Re-running until nothing changes converges to the correct single backslash
    regardless of how many doubling passes the original corruption went
    through, without needing to special-case 4-vs-2 in the regex itself."""
    total = 0
    for _ in range(max_passes):
        text, n = fix_text(text)
        total += n
        if n == 0:
            break
    return text, total


def main():
    dry = "--dry-run" in sys.argv
    files = sorted(p for p in PAPERS_DIR.rglob("*.md"))
    total_fixed_files = 0
    total_edits = 0
    log_path = Path("D:/tmp/doubled_backslash_fix_report.txt")
    with io.open(log_path, "w", encoding="utf-8") as log:
        for f in files:
            text = f.read_text(encoding="utf-8")
            new_text, n = fix_text_to_fixed_point(text)
            if n:
                total_fixed_files += 1
                total_edits += n
                if not dry:
                    f.write_text(new_text, encoding="utf-8")
                log.write(f"{'[dry] ' if dry else ''}{f.relative_to(ROOT)}: {n} backslash fix(es)\n")
        log.write(f"\n{'[DRY RUN] ' if dry else ''}files touched: {total_fixed_files}, total edits: {total_edits}\n")
    print(f"done, see {log_path} — files touched: {total_fixed_files}, total edits: {total_edits}")


if __name__ == "__main__":
    main()
