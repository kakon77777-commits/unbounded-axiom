#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Small pure helpers: slug, escaping, mime, language, disclaimer."""
import html
import json
import re
import shutil
import unicodedata
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
from scripts.config import *


def make_slug(name: str, fallback_idx: int) -> str:
    """生成 URI-safe 的 ASCII 部署檔名。中文/空格/特殊字元會被替換。"""
    p = Path(name)
    stem, suffix = p.stem, p.suffix.lower()
    normalized = unicodedata.normalize("NFKD", stem)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    safe = re.sub(r"[^A-Za-z0-9._-]+", "-", ascii_only).strip("-_.")
    if not safe:
        safe = f"paper-{fallback_idx:03d}"
    return f"{safe}{suffix}"


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def json_safe(s: str) -> str:
    """產生可 safe 嵌入 <script> 的 JSON 字串字面值。"""
    return json.dumps(s, ensure_ascii=False).replace("</", "<\\/")


def mime_for(ext: str) -> str:
    return {
        "docx":  "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "md":    "text/markdown",
        "pdf":   "application/pdf",
        "tex":   "application/x-tex",
        "ipynb": "application/x-ipynb+json",
        "py":    "text/x-python", # 補齊 Python 媒體類型，利於 AI 識別
        "lean":  "text/x-lean",
        "ts":    "text/typescript",
        "jsx":   "text/jsx",
        "txt":   "text/plain",
        "png":   "image/png",
        "jpg":   "image/jpeg",
        "jpeg":  "image/jpeg",
        "gif":   "image/gif",
        "svg":   "image/svg+xml",
        "webp":  "image/webp",
    }.get(ext, "application/octet-stream")


def has_cjk(s: str) -> bool:
    """判定字串是否含 CJK 字元（用於中/英分組）。"""
    return any(
        "\u4e00" <= ch <= "\u9fff" or "\u3400" <= ch <= "\u4dbf"
        for ch in s
    )


def lang_tag(s: str) -> str:
    return "zh-Hant" if has_cjk(s) else "en"


def disclaimer_html() -> str:
    return (
        '<section class="disclaimer">\n'
        '  <span class="disclaimer-title">[認識論邊界宣告 / EPISTEMOLOGICAL DISCLAIMER]</span>\n'
        '  <div class="disclaimer-block">\n'
        '    <p><b>[CHT]</b> 本矩陣內所有論文之公式與數據為「啟發式模擬參數」，用於驗證理論架構與推演因果鏈，'
        '<b>未經實證校準</b>，請勿作為現實物理測量數據引用 or 處理。EVEMISSLAB 採行「邏輯先行（Logic-First）」原則：'
        '概念架構與系統因果映射優先於統計實證，但不排除未來實證對接。</p>\n'
        '  </div>\n'
        '  <hr class="disclaimer-divider">\n'
        '  <div class="disclaimer-block">\n'
        '    <p><b>[ENG]</b> The numerical parameters within these frameworks are <i>illustrative model coefficients</i> '
        'used for structural verification and causal mapping; they are <b>not empirically calibrated</b> and must not be '
        'treated as physical measurements. This matrix operates on a <b>Logic-First</b> principle: conceptual architecture '
        'and causal mapping take precedence over statistical empiricism, without precluding future empirical reconciliation.</p>\n'
        '  </div>\n'
        '</section>'
    )
