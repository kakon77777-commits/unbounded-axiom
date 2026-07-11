#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GEO layer — Generative/Answer-Engine Optimization signals (docs/AI-Native 論文寫作規範.md).

Detects two opt-in authoring conventions directly in a paper's RAW MARKDOWN SOURCE
(not the rendered HTML — that varies by renderer/backend; the source text is the one
thing every render path agrees on) and turns them into explicit schema.org structured
data instead of leaving AI/answer engines to infer structure themselves:

- Answer-first Q&A H2 node: a "## " heading that is a genuine question (ends in ?/？),
  whose first paragraph is a self-contained answer -> schema.org FAQPage.
- Self-contained definition block: a single-line blockquote opening with
  "**定義｜term**" / "**Definition｜term**" -> schema.org DefinedTermSet.

Both are opt-in by content shape: papers that don't use the convention emit no extra
schema. Mirrors the warn-only pattern of validate.py's broken-link report — this
writes registry/generated/geo-lint.json flagging blocks that violate the
self-containment budget, without failing the build.
"""
import json
import re

from scripts.config import *

REGISTRY_DIR = ROOT / "registry"
GEN_DIR = REGISTRY_DIR / "generated"

_H2_QUESTION = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
_HEADING_ANY = re.compile(r"^#{1,6}\s+")
_DEFINITION = re.compile(
    r"^>\s*\*\*(?:定義|Definition)\s*[｜:：]\s*(.+?)\*\*\s*[:：]?\s*(.*)$",
    re.MULTILINE | re.IGNORECASE,
)
_MD_EMPHASIS = re.compile(r"\*\*([^*]+)\*\*|\*([^*]+)\*|`([^`]+)`")

_TOKEN_BUDGET = 220           # soft ceiling; convention target is ~200 tokens/block
_THIN_ANSWER_TOKENS = 8       # answers shorter than this aren't really "answers"


def _strip_emphasis(text: str) -> str:
    return _MD_EMPHASIS.sub(lambda m: next(g for g in m.groups() if g is not None), text).strip()


def _looks_like_question(heading: str) -> bool:
    h = heading.strip()
    return h.endswith("?") or h.endswith("？")


def _token_estimate(text: str) -> int:
    """CJK chars ~1 token each; everything else ~1 token per 4 chars."""
    cjk = sum(1 for ch in text if "一" <= ch <= "鿿" or "㐀" <= ch <= "䶿")
    rest = len(text) - cjk
    return cjk + rest // 4


def extract_geo_signals(md_source: str) -> dict:
    """Scan raw markdown source for Q&A H2 nodes and self-contained definition blocks."""
    lines = md_source.replace("\r\n", "\n").split("\n")

    qa = []
    for m in _H2_QUESTION.finditer(md_source):
        heading = m.group(1).strip()
        if not _looks_like_question(heading):
            continue
        start_line = md_source.count("\n", 0, m.end()) + 1
        answer_lines = []
        for ln in lines[start_line:]:
            if not ln.strip():
                if answer_lines:
                    break
                continue
            if _HEADING_ANY.match(ln):
                break
            answer_lines.append(ln.strip())
        answer = _strip_emphasis(" ".join(answer_lines))
        if answer:
            qa.append({"question": _strip_emphasis(heading), "answer": answer})

    definitions = []
    for m in _DEFINITION.finditer(md_source):
        term = _strip_emphasis(m.group(1).strip())
        body = _strip_emphasis(m.group(2).strip())
        if term and body:
            definitions.append({"term": term, "body": body})

    return {"qa": qa, "definitions": definitions}


def geo_jsonld_blocks(signals: dict, canonical: str) -> list:
    """Extra JSON-LD objects (FAQPage / DefinedTermSet) for a page. Empty list if no signals."""
    blocks = []
    if signals["qa"]:
        blocks.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": item["question"],
                    "acceptedAnswer": {"@type": "Answer", "text": item["answer"]},
                }
                for item in signals["qa"]
            ],
        })
    if signals["definitions"]:
        blocks.append({
            "@context": "https://schema.org",
            "@type": "DefinedTermSet",
            "@id": f"{canonical}#definitions",
            "hasDefinedTerm": [
                {
                    "@type": "DefinedTerm",
                    "name": d["term"],
                    "description": d["body"],
                    "inDefinedTermSet": f"{canonical}#definitions",
                }
                for d in signals["definitions"]
            ],
        })
    return blocks


def jsonld_script_tags(blocks: list) -> str:
    out = []
    for block in blocks:
        payload = json.dumps(block, ensure_ascii=False, indent=2).replace("</", "<\\/")
        out.append(f'<script type="application/ld+json">\n{payload}\n</script>\n')
    return "".join(out)


def lint_signals(item_id: str, signals: dict, findings: list) -> None:
    for d in signals["definitions"]:
        tok = _token_estimate(d["body"])
        if tok > _TOKEN_BUDGET:
            findings.append({"id": item_id, "type": "definition_too_long",
                              "term": d["term"], "estimated_tokens": tok, "budget": _TOKEN_BUDGET})
        if d["term"] not in d["body"]:
            findings.append({"id": item_id, "type": "definition_not_self_restating",
                              "term": d["term"]})
    for item in signals["qa"]:
        tok = _token_estimate(item["answer"])
        if tok < _THIN_ANSWER_TOKENS:
            findings.append({"id": item_id, "type": "qa_answer_too_thin",
                              "question": item["question"], "estimated_tokens": tok})


def write_geo_layer(registry, entries) -> dict:
    """Scan every .md paper's raw source, return {id: signals} for pages that have
    any, and write the warn-only geo-lint report."""
    src_by_relpath = {src.relative_to(ROOT).as_posix(): src for _, _, ext, src in entries if ext == "md"}
    per_id = {}
    findings = []
    scanned = 0
    with_signals = 0
    for item in registry["items"]:
        if item["ext"] != "md":
            continue
        src = src_by_relpath.get(item["source_file"])
        if not src:
            continue
        scanned += 1
        try:
            text = src.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        signals = extract_geo_signals(text)
        if not (signals["qa"] or signals["definitions"]):
            continue
        with_signals += 1
        per_id[item["id"]] = signals
        lint_signals(item["id"], signals, findings)

    GEN_DIR.mkdir(parents=True, exist_ok=True)
    (GEN_DIR / "geo-lint.json").write_text(json.dumps({
        "version": "0.1",
        "phase": "warn-only",
        "convention": "docs/AI-Native 論文寫作規範.md",
        "md_papers_scanned": scanned,
        "papers_with_signals": with_signals,
        "finding_count": len(findings),
        "findings": findings[:500],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return {"per_id": per_id, "scanned": scanned, "with_signals": with_signals, "findings": findings}
