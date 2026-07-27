#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dynamic Semantic Revealing — Phase 2 concept dictionary (§7 of lm-001785).

Build-time generated, like the Phase 0+1 index in semantic_layer.py — this is
NOT a hand-authored file, so it grows automatically as the corpus and its
Research Programs grow, with no separate maintenance step.

Two zero-guess sources only, per this project's standing rule ("近似必須被
標示" — never assert an expansion I can't point to real evidence for):

  1. Research Programs (registry/programs/*.json): each Program's
     title / short_title / title_en are already a curated alias set (I wrote
     them myself when building the Program). source: system_inferred (I'm
     repurposing already-curated data programmatically, not a human
     reviewing a dictionary specifically) — never claimed as editor_confirmed.

  2. Self-defining acronym titles: many papers in this corpus title
     themselves "ACRONYM_CJK全名_..." or "CJK全名_ACRONYM_..." — the acronym
     and its expansion appear PAIRED in the paper's own published title, so
     extracting the pair isn't a guess, it's reading what the author already
     wrote. Ambiguous/ambiguous-looking hits are hand-excluded below rather
     than silently trusted — see EXCLUDED_ACRONYMS for why each one is out.

Outputs:
    registry/generated/semantic-dictionary.raw.json   full records (readable)
    dist/ai/semantic-dictionary.min.json               compressed, served
"""
import json
import re
from datetime import datetime, timezone

from scripts.config import *
from scripts.programs import load_program_seeds

GENERATED_DIR = ROOT / "registry" / "generated"

# The CJK-name capture must end at a real naming-construct boundary — a
# version marker (_v0.1), an underscore, a colon, or end of string — NOT a
# bare space, which the first cut of this extractor used and which happily
# matched an acronym sitting in the middle of an ordinary sentence ("小模型
# 開源訓練作為高 ROI 時代槓桿", "為什麼 AIAGI 需要正確的自我本體論") as if it
# were a structured self-definition. Tightening to a real boundary is what
# separates "MCDM_v0.1" (a title labeling itself) from "... 高 ROI 時代 ..."
# (ROI is just an English loanword mid-prose).
_BOUNDARY = r"(?:_v\d|[_：:]|$)"
ACRONYM_THEN_NAME_RE = re.compile(r"^([A-Z]{2,8})[_\s]([一-鿿]{4,20})" + _BOUNDARY)
NAME_THEN_ACRONYM_RE = re.compile(r"^([一-鿿]{3,24})[_\s]([A-Z]{2,8})" + _BOUNDARY)

# Trim generic boilerplate a title tacks onto the real concept name. Longest
# first: "技術白皮書" must be tried whole before its own tail "白皮書", or the
# short suffix fires on the name's leftover tail and mangles it (observed:
# name=="技術白皮書" survived the "technic白皮書" whole-suffix check because it
# wasn't LONGER than the suffix, then the shorter "白皮書" suffix trimmed it
# down to a meaningless "技術").
GENERIC_SUFFIXES = sorted(
    ["技術白皮書", "理論草稿", "概念論文", "白皮書", "論文", "總論", "系列索引"],
    key=len, reverse=True,
)
MIN_NAME_LENGTH = 4  # below this a trimmed/extracted name is noise, not a concept

# Acronyms found by the patterns above but excluded from the dictionary:
#   AI     — not a corpus-specific acronym, matches almost anything, useless as a "concept"
#   AGI    — established external term (Artificial General Intelligence); this corpus's own
#            "脈衝式 AGI 演化模型" paper uses the standard sense, not a private redefinition,
#            so a dictionary entry would be redundant at best and misleading at worst
#   PCMT   — two different papers pair it with two different CJK names (七十二格計算動力學
#            vs 二十四計算範式) — genuinely ambiguous, don't assert either as THE expansion
#   MBTI   — this corpus's own paper redefines a well-known external acronym for an
#            unrelated internal concept; exact-title search already finds the paper without
#            a dictionary entry, and a dictionary entry risks implying the corpus's private
#            sense is interchangeable with the famous one when someone types "MBTI"
#   ASI    — same overload concern as MBTI (Artificial Superintelligence is an established
#            external term this corpus's "類終極" paper is not simply a synonym for)
#   SOS    — extraction was technically accurate (組合安全性規格 = Composition Safety Spec)
#            but "SOS" the universal distress signal is too overloaded a token to alias
#   ANLA   — external knowledge (this is Neo's own separate project, "Agent-Native Lossless
#            Archive") contradicts what the title-pattern extracted ("從無損封裝到可攜認知
#            宇宙" is that paper's subtitle/trajectory description, not ANLA's expansion) —
#            a case where the mechanical pattern was wrong and had to be caught by hand
#   ARCP   — namespace collision with Neo's OWN separate ARCP project (兩個家 whitepapers,
#            a different concept entirely) — this paper's local "通用網頁端自主...Agent"
#            usage would alias the wrong thing if merged with that other project's sense
#   FDRS   — extraction paired it with "容器同一性", which reads as a specific demo's
#            subtopic ("container-identity demonstration"), not FDRS's own canonical name —
#            genuinely uncertain, exclude rather than assert
#   WT     — the source title is "WT 視角下的底空間世界束展開論" ("the theory of ... from
#            WT's PERSPECTIVE") — 視角下的 is a grammatical construction ("from the
#            perspective of"), not part of a name; the extractor caught the sentence's
#            subject, not a definition
EXCLUDED_ACRONYMS = {"AI", "AGI", "PCMT", "MBTI", "ASI", "SOS", "ANLA", "ARCP", "FDRS", "WT"}

_ROMAN_NUMERAL_RE = re.compile(r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")


def _looks_like_roman_numeral(s: str) -> bool:
    """Series numbering ("...III：...", "第 IV 部") matches [A-Z]{2,8} just as
    well as a real acronym does — filter it out before it becomes a fake concept."""
    return bool(s) and bool(_ROMAN_NUMERAL_RE.match(s))


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _clean_name(name: str) -> str | None:
    if name in GENERIC_SUFFIXES:
        return None  # the "name" IS just boilerplate, nothing real underneath it
    for suf in GENERIC_SUFFIXES:
        if name.endswith(suf) and len(name) > len(suf) + 1:
            name = name[: -len(suf)]
            break  # longest-first order: stop after the first (longest) match,
                    # don't let a shorter suffix re-trim the already-trimmed result
    name = name.strip("_ ：:")
    return name if len(name) >= MIN_NAME_LENGTH else None


def _slugify(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9一-鿿]+", "-", s).strip("-").lower()
    return s or "concept"


def _acronym_entries(registry) -> list:
    seen_acronyms = {}
    for it in registry["items"]:
        title = it["title"]
        m = ACRONYM_THEN_NAME_RE.match(title)
        if m:
            acro, name = m.group(1), _clean_name(m.group(2))
        else:
            m = NAME_THEN_ACRONYM_RE.match(title)
            if not m:
                continue
            name, acro = _clean_name(m.group(1)), m.group(2)
        if acro in EXCLUDED_ACRONYMS or not name or _looks_like_roman_numeral(acro):
            continue
        # first sighting wins; later duplicate acronyms with a DIFFERENT name are
        # dropped entirely (ambiguous, matching the PCMT exclusion reasoning above)
        # rather than silently overwritten.
        if acro in seen_acronyms:
            if seen_acronyms[acro][0] != name:
                seen_acronyms[acro] = None  # mark ambiguous, drop later
            continue
        seen_acronyms[acro] = (name, it["id"])

    entries = []
    for acro, val in seen_acronyms.items():
        if val is None:
            continue
        name, source_id = val
        entries.append({
            "concept_id": f"concept-{_slugify(acro)}",
            "canonical": name,
            "aliases": [{"term": acro, "weight": 0.92}],
            "related": [],
            "broader": [],
            "narrower": [],
            "status": "system_inferred",
            "evidence": {"source_paper_id": source_id, "method": "self_defining_title_pattern"},
        })
    return entries


def _program_entries() -> list:
    entries = []
    for seed in load_program_seeds():
        canonical = seed.get("title")
        if not canonical:
            continue
        aliases = []
        short = seed.get("short_title")
        if short and short != canonical:
            aliases.append({"term": short, "weight": 0.90})
        title_en = seed.get("title_en")
        if title_en and title_en != canonical:
            aliases.append({"term": title_en, "weight": 0.85})
        if not aliases:
            continue
        entries.append({
            "concept_id": f"concept-{seed['id']}",
            "canonical": canonical,
            "aliases": aliases,
            "related": [],
            "broader": [],
            "narrower": [],
            "status": "system_inferred",
            "evidence": {"source_program_id": seed["id"], "method": "program_title_fields"},
        })
    return entries


def build_dictionary(registry) -> list:
    return _program_entries() + _acronym_entries(registry)


def write_semantic_dictionary(registry, build_id=None) -> dict:
    entries = build_dictionary(registry)

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    (GENERATED_DIR / "semantic-dictionary.raw.json").write_text(
        json.dumps({"generated_at": _now(), "count": len(entries), "entries": entries},
                   ensure_ascii=False, indent=2),
        encoding="utf-8")

    compact = [
        {
            "concept_id": e["concept_id"],
            "canonical": e["canonical"],
            "aliases": e["aliases"],
            "related": e["related"],
        }
        for e in entries
    ]
    payload = {
        "schema_version": "0.1",
        "generated_at": _now(),
        "build_id": build_id,
        "count": len(compact),
        "note": "Dynamic Semantic Revealing concept dictionary (Phase 2, §7 of "
                "lm-001785). Every entry is system_inferred — either a Research "
                "Program's own title/short_title/title_en fields, or an acronym "
                "self-defined in a paper's own title (\"ACRONYM_全名_...\" or the "
                "reverse). No entry is a guessed or model-hallucinated expansion.",
        "entries": compact,
    }
    ai_dir = DIST_DIR / "ai"
    ai_dir.mkdir(parents=True, exist_ok=True)
    out_path = ai_dir / "semantic-dictionary.min.json"
    out_text = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    out_path.write_text(out_text, encoding="utf-8")

    return {"count": len(entries), "bytes": len(out_text.encode("utf-8"))}
