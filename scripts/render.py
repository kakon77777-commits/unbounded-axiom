#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Markdown/source rendering and body/raw-text extraction."""
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
from scripts.helpers import *


try:
    import markdown as _MD_LIB

    def render_markdown(text: str) -> str:
        return _MD_LIB.markdown(text, extensions=["fenced_code", "tables", "toc"])
    _MD_BACKEND = "markdown-lib"
except Exception:                      # fallback：內建極簡渲染器
    _MD_BACKEND = "builtin-minimal"

    def _inline(s: str) -> str:
        code: list[str] = []

        def stash(m):
            code.append(m.group(1))
            return f"\x00{len(code) - 1}\x00"

        s = re.sub(r"`([^`]+)`", stash, s)
        s = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", r'<img src="\2" alt="\1">', s)
        s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2" rel="noopener">\1</a>', s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"__([^_]+)__", r"<strong>\1</strong>", s)
        s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
        s = re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"<em>\1</em>", s)
        s = re.sub(r"\x00(\d+)\x00", lambda m: "<code>" + code[int(m.group(1))] + "</code>", s)
        return s

    def render_markdown(text: str) -> str:
        lines = text.replace("\r\n", "\n").split("\n")
        out: list[str] = []
        para: list[str] = []
        list_type = None
        i = 0

        def flush_para():
            if para:
                out.append("<p>" + _inline(esc(" ".join(para))) + "</p>")
                para.clear()

        def close_list():
            nonlocal list_type
            if list_type:
                out.append(f"</{list_type}>")
                list_type = None

        while i < len(lines):
            ln = lines[i]
            if ln.strip().startswith("```"):
                flush_para(); close_list()
                i += 1
                buf = []
                while i < len(lines) and not lines[i].strip().startswith("```"):
                    buf.append(lines[i]); i += 1
                i += 1
                out.append("<pre><code>" + esc("\n".join(buf)) + "</code></pre>")
                continue
            st = ln.strip()
            if not st:
                flush_para(); close_list(); i += 1; continue
            hm = re.match(r"^(#{1,6})\s+(.*)$", st)
            if hm:
                flush_para(); close_list()
                lvl = len(hm.group(1))
                out.append(f"<h{lvl}>" + _inline(esc(hm.group(2))) + f"</h{lvl}>")
                i += 1; continue
            if re.match(r"^([*\-_]\s*){3,}$", st):
                flush_para(); close_list(); out.append("<hr>"); i += 1; continue
            if st.startswith(">"):
                flush_para(); close_list()
                out.append("<blockquote>" + _inline(esc(st.lstrip("> ").strip())) + "</blockquote>")
                i += 1; continue
            um = re.match(r"^[-*+]\s+(.*)$", st)
            if um:
                flush_para()
                if list_type != "ul":
                    close_list(); out.append("<ul>"); list_type = "ul"
                out.append("<li>" + _inline(esc(um.group(1))) + "</li>")
                i += 1; continue
            om = re.match(r"^\d+\.\s+(.*)$", st)
            if om:
                flush_para()
                if list_type != "ol":
                    close_list(); out.append("<ol>"); list_type = "ol"
                out.append("<li>" + _inline(esc(om.group(1))) + "</li>")
                i += 1; continue
            close_list()
            para.append(st)
            i += 1
        flush_para(); close_list()
        return "\n".join(out)


def extract_body(src: Path, ext: str):
    """回傳 (body_html, mode)。mode: 'full'(全文) | 'source'(原始碼) | 'landing'(僅落地)。"""
    try:
        if ext == "md":
            return render_markdown(src.read_text(encoding="utf-8", errors="replace")), "full"
        if ext == "ipynb":
            nb = json.loads(src.read_text(encoding="utf-8", errors="replace"))
            parts = []
            for cell in nb.get("cells", []):
                txt = "".join(cell.get("source", []))
                if cell.get("cell_type") == "markdown":
                    parts.append(render_markdown(txt))
                elif cell.get("cell_type") == "code":
                    parts.append("<pre><code>" + esc(txt) + "</code></pre>")
            return "\n".join(parts) or None, "full" if parts else "landing"
        
        # 【修正二】讓 .py 與 .tex 完美共享高保真原始碼檢視通道
        if ext in ("tex", "py", "lean", "ts", "jsx"):
            return "<pre><code>" + esc(src.read_text(encoding="utf-8", errors="replace")) + "</code></pre>", "source"
            
        if ext == "docx":
            with zipfile.ZipFile(src) as z:
                xml = z.read("word/document.xml").decode("utf-8", "replace")
            html_paras = []
            for chunk in re.split(r"</w:p>", xml):
                texts = re.findall(r"<w:t[^>]*>(.*?)</w:t>", chunk, re.DOTALL)
                line = esc("".join(texts)).strip()
                if line:
                    html_paras.append("<p>" + line + "</p>")
            return ("\n".join(html_paras), "full") if html_paras else (None, "landing")
    except Exception:
        return None, "landing"
    return None, "landing"


def extract_raw_text(src: Path, ext: str) -> str:
    try:
        if ext == "md":
            return src.read_text(encoding="utf-8", errors="replace")
        if ext in ("py", "tex", "lean", "ts", "jsx"):
            code = src.read_text(encoding="utf-8", errors="replace")
            return f"```{ext}\n{code}\n```"
        if ext == "ipynb":
            nb = json.loads(src.read_text(encoding="utf-8", errors="replace"))
            parts = []
            for cell in nb.get("cells", []):
                txt = "".join(cell.get("source", []))
                ctype = cell.get("cell_type")
                if ctype == "markdown":
                    parts.append(txt)
                elif ctype == "code":
                    parts.append(f"```python\n{txt}\n```")
            return "\n\n".join(parts)
        if ext == "docx":
            with zipfile.ZipFile(src) as z:
                xml = z.read("word/document.xml").decode("utf-8", "replace")
            paras = []
            for chunk in re.split(r"</w:p>", xml):
                texts = re.findall(r"<w:t[^>]*>(.*?)</w:t>", chunk, re.DOTALL)
                line = "".join(texts).strip()
                if line:
                    paras.append(line)
            return "\n\n".join(paras)
        if ext == "pdf":
            return f"*[PDF Binary Document - Available for download at {SITE_URL}/papers/{quote(src.name)}]*"
    except Exception as e:
        return f"*[Error extracting text from {src.name}: {str(e)}]*"
    return f"*[Binary or Unsupported format: {ext}]*"
