#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""One-time repair script: inside row/column environments (`cases`,
`aligned`, `align`, `array`), a lone `\ ` (single backslash + space)
sometimes sits where the row-separator `\\` (double backslash) should be —
the corruption seems to have dropped one of the two backslashes specifically
at row boundaries. Distinct from the "every command backslash got doubled"
bug already fixed — this is the opposite direction, and only inside these
row-structured environments (a genuine `\ ` control-space is common enough
in ordinary prose-math that a blanket global fix would risk false positives;
row separators inside a piecewise/aligned block are a much narrower, safer
target).

Usage: python scripts/_katex_fix_cases_rowsep.py [--dry-run]
"""
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "content" / "papers"

CASES_RE = re.compile(r"\\begin\{(cases|aligned|align\*?|array)\}([\s\S]*?)\\end\{\1\}")
# A single backslash immediately followed by a space, not preceded by another
# backslash. The lookbehind is what keeps this from matching the SECOND
# backslash of a genuine row separator "\\ " — requiring the space right
# after the backslash already guarantees the backslash isn't the FIRST of a
# "\\" pair (if it were, the very next character would be another backslash,
# not a space, so the literal `\ ` in the pattern wouldn't match there at
# all). An earlier version of this pattern also required "not followed by
# another backslash" AFTER the space — that was wrong: it's exactly what
# blocked the real target case, a lone `\ ` immediately followed by a
# separate `\text{...}` command ("\epsilon \ \text{FreeAbort}"), by
# mistaking two adjacent-but-separate backslash tokens for one \\ pair.
LONE_BACKSLASH_SPACE_RE = re.compile(r"(?<!\\)\\ ")


def fix_block(inner: str) -> tuple[str, int]:
    return LONE_BACKSLASH_SPACE_RE.subn(r"\\\\ ", inner)


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
    log_path = Path("D:/tmp/cases_rowsep_fix_report.txt")
    with io.open(log_path, "w", encoding="utf-8") as log:
        for f in files:
            text = f.read_text(encoding="utf-8")
            new_text, n = fix_text(text)
            if n:
                total_fixed_files += 1
                total_edits += n
                if not dry:
                    f.write_text(new_text, encoding="utf-8")
                log.write(f"{'[dry] ' if dry else ''}{f.relative_to(ROOT)}: {n} row-sep fix(es)\n")
        log.write(f"\n{'[DRY RUN] ' if dry else ''}files touched: {total_fixed_files}, total edits: {total_edits}\n")
    print(f"done, see {log_path} — files touched: {total_fixed_files}, total edits: {total_edits}")


if __name__ == "__main__":
    main()
