"""Content-review a staged paper via Gemini 3.7 Flash (Vertex AI backend)
instead of a Claude Agent-tool sub-agent, to conserve Claude usage. Encodes
the same checklist this project's Claude review agents have used across 10
batches.

Usage:
    python3 scripts/gemini_paper_review.py "ingest/01-before/<file>.md"
    python3 scripts/gemini_paper_review.py "ingest/01-before/<file>.md" --apply

Credentials: reuses the existing service account key at
D:\\Ai\\work together\\google-genai\\gcp-key.json (already provisioned; that
folder was "Google_Vertex AI" until 2026-08-19, renamed to match Google's
own SDK rebrand from google-cloud-aiplatform to google-genai).
"""
import argparse
import json
import os
import sys
from pathlib import Path

from google import genai
from google.genai import types

VERTEX_DIR = Path(r"D:\Ai\work together\google-genai")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(VERTEX_DIR / "gcp-key.json")

PROJECT_ID = "tidy-arcade-498907-s5"
LOCATION = "global"
MODEL_ID = "gemini-3.7-flash"

SYSTEM_PROMPT = """You are doing careful MECHANICAL/STRUCTURAL content review of one academic \
theory paper (Traditional Chinese, with inline LaTeX math) for a corpus site. You are NOT a peer \
reviewer of the ideas -- do not evaluate whether the theory is correct, do not suggest content \
changes. Only find MECHANICAL defects from this exact checklist, each one previously found \
recurring in this corpus across many prior batches:

1. LaTeX corruption:
   - a missing `\\boxed{` opener before a closing `$` (the paired `}` survives, orphaned)
   - `\\boxed{` that opens but never closes because an inner `\\textbf{}`/`\\text{}` closes first
   - bare custom relation/predicate symbols used as if real LaTeX commands, without `\\text{}`/
     `\\operatorname{}` wrapping (but do NOT flag single-letter variables or an established,
     consistently-used bare-CamelCase house style within the SAME file -- only flag genuine
     one-off inconsistencies against that file's own convention)
   - missing `\\Rightarrow` between `\\not` and a following word (note: `\\notin`, `\\not\\equiv`
     etc. are correct single/paired commands, NOT this defect)
   - a dropped leading letter from a two-character Greek LaTeX command, e.g. `\\nu` losing its
     leading `\\n` and leaving a stray duplicated letter like `u` nearby
   - `aligned`/`align` environment rows using a single trailing `\\` instead of the required `\\\\`
     row separator
   - bare math-mode English words (`fail`, `false`, `true`) needing `\\mathrm{}`/`\\text{}` wrapping

2. Markdown list-marker defects: a list where the first item is `- item` (dash+space, correct)
   but subsequent items in the SAME list are `-item` (dash, no space) -- CommonMark requires the
   space, so those items silently collapse into run-on paragraph text. Do not flag legitimate
   negative signs/numbers inside math blocks (e.g. `-\\frac13`, `-1000`).

3. PUA-Unicode-wrapped AI-research-tool citation artifacts: leftover fragments like
   `citeturn423235view1turn183230search29`, wrapped in Unicode Private-Use-Area control
   characters (U+E000-F8FF), invisible in normal viewing.

4. Simplified-Chinese characters mixed into this Traditional-Chinese text (e.g. 与/个/远/对/
   后/时/须/将/准确/众/仅/别(as 别) in place of the Traditional forms). Do NOT flag characters
   that are legitimate standard Traditional usage even if they happen to also exist as PRC
   simplified forms elsewhere (e.g. 群, 才, 只, 准 in "不准", 布 in "宣布" are all correct
   Traditional Chinese as-is -- only flag genuine simplification substitutions). IMPORTANT: when
   a sentence/word contains MULTIPLE simplified characters, your corrected_text must fix EVERY
   one of them, not just the first -- re-scan your own corrected_text character-by-character
   before finalizing each finding to confirm no simplified character remains in it.

5. Foreign-script contamination: a stray non-CJK, non-Latin-script character embedded mid-
   Chinese-prose -- most commonly a Devanagari danda "।" (U+0964) standing in for the Chinese
   full stop "。".

6. Structural issues: broken/duplicated headers, encoding mojibake, truncated sections,
   malformed tables.

For EVERY finding, give: the defect category, a short unique anchor (a short exact quoted
substring from the file that appears ONLY at the defect location, long enough to be unambiguous),
the broken original text, and the exact corrected replacement text. Do not paraphrase the anchor
or original text -- copy it byte-for-byte from the document.

Also report whether the paper is substantive (real argumentative/theoretical content) or a stub/
non-paper, and a one-sentence summary of what you checked.

Return ONLY the structured JSON response. No prose outside the JSON."""

RESPONSE_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "substantive": {"type": "BOOLEAN"},
        "summary": {"type": "STRING"},
        "findings": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "category": {"type": "STRING"},
                    "anchor": {"type": "STRING"},
                    "original_text": {"type": "STRING"},
                    "corrected_text": {"type": "STRING"},
                    "explanation": {"type": "STRING"},
                },
                "required": ["category", "anchor", "original_text", "corrected_text", "explanation"],
            },
        },
    },
    "required": ["substantive", "summary", "findings"],
}


_client = None


def get_client():
    global _client
    if _client is None:
        _client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
    return _client


def review_paper(filepath: Path, max_output_tokens: int = 65535) -> dict:
    # Free Vertex AI credits (~NT$30k+), not metered against Claude usage --
    # generous budgets are the default, not a cost corner to cut.
    text = filepath.read_text(encoding="utf-8")
    response = get_client().models.generate_content(
        model=MODEL_ID,
        contents=SYSTEM_PROMPT + "\n\n--- DOCUMENT (" + filepath.name + ") ---\n\n" + text,
        config=types.GenerateContentConfig(
            max_output_tokens=max_output_tokens,
            response_mime_type="application/json",
            response_json_schema=RESPONSE_SCHEMA,
            thinking_config=types.ThinkingConfig(thinking_budget=8192),
        ),
    )
    cand = response.candidates[0]
    finish_reason = str(cand.finish_reason) if cand.finish_reason else None
    usage = response.usage_metadata.model_dump(exclude_none=True) if response.usage_metadata else {}
    text_out = response.text or ""
    if not text_out:
        return {"error": "empty_response", "finishReason": finish_reason, "usage": usage}
    try:
        parsed = json.loads(text_out)
    except json.JSONDecodeError as e:
        return {"error": f"json_decode_error: {e}", "finishReason": finish_reason, "usage": usage, "raw_text": text_out}
    parsed["_usage"] = usage
    parsed["_finishReason"] = finish_reason
    return parsed


def apply_findings(filepath: Path, findings: list) -> list:
    text = filepath.read_text(encoding="utf-8")
    applied, skipped = [], []
    for f in findings:
        orig = f["original_text"]
        if text.count(orig) == 1:
            text = text.replace(orig, f["corrected_text"], 1)
            applied.append(f)
        else:
            skipped.append((f, text.count(orig)))
    filepath.write_text(text, encoding="utf-8")
    return applied, skipped


if __name__ == "__main__":
    # Windows terminals default to cp950 for stdout, which cannot encode most
    # CJK punctuation/symbols used in these papers -> crashes on print(). Force
    # UTF-8 stdout/stderr so results are never lost to a cosmetic encoding error.
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

    ap = argparse.ArgumentParser()
    ap.add_argument("filepath")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--out", help="write JSON result to this file instead of stdout")
    args = ap.parse_args()

    fp = Path(args.filepath)
    result = review_paper(fp)
    out_text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_text(out_text, encoding="utf-8")
        print(f"wrote result to {args.out}")
    else:
        print(out_text)

    if args.apply and "findings" in result:
        applied, skipped = apply_findings(fp, result["findings"])
        print(f"\napplied={len(applied)} skipped={len(skipped)}", file=sys.stderr)
        for f, count in skipped:
            print(f"  SKIPPED (anchor count={count}): {f['category']} - {f['anchor'][:60]}", file=sys.stderr)
