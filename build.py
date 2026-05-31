#!/usr/bin/env python3
"""
EVEMISSLAB Logic Matrix — Build Script (AIO-v3.0)
AIO-oriented static site builder for the EveMissLab theoretical corpus.

v3.0 新增（AI 流量導向）：
  - 每篇論文渲染為「可被引用的 HTML 頁」（per-paper），帶 ScholarlyArticle JSON-LD
  - .md 全文渲染；.ipynb/.docx/.tex 安全抽取；.pdf 落地頁 + 內嵌/下載
  - 原始檔仍保留，並以 <link rel="alternate"> 掛在 HTML 頁上（供 RAG 取用）
  - 同一 HTML URL 對人對 bot 給同樣內容（非 bot-specific，避免 cloaking）
  - index / sitemap / llms.txt 改指向 HTML 頁（正規可引用 URL）
  - 無外部依賴：有 markdown 套件則用之，否則用內建極簡渲染器 fallback

保留自前版：URI-safe slug、CJK 標題保留、遞歸掃描、衝突處理、雙語免責、robots。
"""
import html
import json
import re
import shutil
import unicodedata
import zipfile
from pathlib import Path
from urllib.parse import quote

# ========== 設定（可改）==========
ROOT = Path(__file__).resolve().parent
PAPERS_DIR = ROOT / "papers"
DIST_DIR = ROOT / "dist"

SUPPORTED_EXTS = {".docx", ".md", ".pdf", ".tex", ".ipynb"}

SITE_TITLE   = "EVEMISSLAB Logic Matrix"
SITE_VERSION = "V2.1"
SITE_TAGLINE = "EveMissLab Theoretical Corpus Access Point"
SITE_URL = "https://logic.evemisslab.com"   # ← 改成你的實際網域
SITE_AUTHOR  = "Neo.K (許筌崴)"
SITE_ORG     = "EveMissLab / 一言諾科技有限公司"

# ========== 工具函數 ==========

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
    """產生可安全嵌入 <script> 的 JSON 字串字面值。"""
    return json.dumps(s, ensure_ascii=False).replace("</", "<\\/")


def mime_for(ext: str) -> str:
    return {
        "docx":  "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "md":    "text/markdown",
        "pdf":   "application/pdf",
        "tex":   "application/x-tex",
        "ipynb": "application/x-ipynb+json",
    }.get(ext, "application/octet-stream")


def has_cjk(s: str) -> bool:
    """判定字串是否含 CJK 字元（用於中/英分組）。"""
    return any(
        "\u4e00" <= ch <= "\u9fff" or "\u3400" <= ch <= "\u4dbf"
        for ch in s
    )


def lang_tag(s: str) -> str:
    return "zh-Hant" if has_cjk(s) else "en"


# ========== Markdown 渲染（無外部依賴；有套件則用之）==========

try:
    import markdown as _MD_LIB

    def render_markdown(text: str) -> str:
        return _MD_LIB.markdown(text, extensions=["fenced_code", "tables", "toc"])
    _MD_BACKEND = "markdown-lib"
except Exception:                      # fallback：內建極簡渲染器
    _MD_BACKEND = "builtin-minimal"

    def _inline(s: str) -> str:
        # s 已 HTML-escape；以下在 escape 後的安全文本上做行內替換
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


# ========== 內容抽取 ==========

def extract_body(src: Path, ext: str):
    """回傳 (body_html, mode)。mode: 'full'(全文) | 'source'(原始碼) | 'landing'(僅落地)。
    任何抽取失敗都降級為 'landing'，絕不讓 build 崩。"""
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
        if ext == "tex":
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
    return None, "landing"            # pdf 或未支援


# ========== 共用片段 ==========

def disclaimer_html() -> str:
    return (
        '<section class="disclaimer">\n'
        '  <span class="disclaimer-title">[認識論邊界宣告 / EPISTEMOLOGICAL DISCLAIMER]</span>\n'
        '  <div class="disclaimer-block">\n'
        '    <p><b>[CHT]</b> 本矩陣內所有論文之公式與數據為「啟發式模擬參數」，用於驗證理論架構與推演因果鏈，'
        '<b>未經實證校準</b>，請勿作為現實物理測量數據引用或處理。EVEMISSLAB 採行「邏輯先行（Logic-First）」原則：'
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


PAGE_CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#000; color:#0f0; font-family:'Courier New',monospace; padding:20px; line-height:1.6; }
.header { text-align:center; border:2px solid #0f0; padding:18px; margin-bottom:22px; }
.header h1 { font-size:1.5em; letter-spacing:2px; }
.header p { margin-top:6px; opacity:0.8; font-size:0.9em; }
.disclaimer { border:1px dashed #ff9900; color:#ff9900; padding:14px; margin:0 auto 22px; max-width:1000px; font-size:0.88em; }
.disclaimer-title { font-weight:bold; margin-bottom:10px; display:block; letter-spacing:1px; }
.disclaimer-divider { border:none; border-top:1px dashed #ff9900; margin:12px 0; opacity:0.55; }
article { max-width:1000px; margin:0 auto; border:1px solid #0f0; padding:24px; }
article h1,article h2,article h3,article h4 { margin:18px 0 8px; letter-spacing:1px; }
article h1 { font-size:1.5em; } article h2 { font-size:1.25em; } article h3 { font-size:1.1em; }
article p { margin:10px 0; }
article ul,article ol { margin:10px 0 10px 24px; }
article blockquote { border-left:3px solid #0f0; padding-left:12px; opacity:0.85; margin:10px 0; }
article pre { background:rgba(0,255,0,0.06); border:1px solid #0f0; padding:12px; overflow-x:auto; margin:12px 0; }
article code { background:rgba(0,255,0,0.08); padding:1px 5px; }
article pre code { background:none; padding:0; }
article a { color:#0ff; }
.nav { max-width:1000px; margin:0 auto 16px; font-size:0.9em; }
.nav a { color:#0f0; text-decoration:none; }
.altbar { max-width:1000px; margin:14px auto 0; font-size:0.85em; opacity:0.7; }
.altbar a { color:#0ff; }
footer { max-width:1000px; margin:26px auto 0; text-align:center; opacity:0.5; font-size:0.82em; }
"""


# ========== 主流程 ==========

def main() -> None:
    if not PAPERS_DIR.exists():
        print(f"[warn] {PAPERS_DIR} not found; creating empty directory.")
        PAPERS_DIR.mkdir()

    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir()
    dist_papers = DIST_DIR / "papers"
    dist_papers.mkdir()

    files = sorted(
        p for p in PAPERS_DIR.rglob("*")
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS
    )

    # 複製原檔 + slug + 衝突處理；entries 含 (slug, display, ext, src_path)
    seen: dict[str, Path] = {}
    entries: list[tuple[str, str, str, Path]] = []
    for idx, f in enumerate(files):
        base = make_slug(f.name, idx)
        slug = base
        n = 1
        while slug in seen:
            bp = Path(base)
            slug = f"{bp.stem}-{n}{bp.suffix}"
            n += 1
        seen[slug] = f
        shutil.copy2(f, dist_papers / slug)          # 原檔保留
        entries.append((slug, f.stem, f.suffix.lower().lstrip("."), f))

    zh_entries = sorted([e for e in entries if has_cjk(e[1])], key=lambda x: x[1])
    en_entries = sorted([e for e in entries if not has_cjk(e[1])], key=lambda x: x[1])

    page_count = write_paper_pages(entries, dist_papers)   # 每篇 HTML 可引用頁
    write_index(zh_entries, en_entries)
    write_robots()
    write_llms_txt(zh_entries, en_entries)
    write_sitemap(entries)

    # ===== 診斷輸出 =====
    print(f"[diag] build.py version: AIO-v3.0 (per-paper HTML)")
    print(f"[diag] markdown backend: {_MD_BACKEND}")
    print(f"[diag] source papers/ scanned: {len(files)} files")
    print(f"[diag] dist/papers/ raw files: {len(entries)} | HTML pages: {page_count}")
    print(f"[diag] language split: {len(zh_entries)} zh-Hant / {len(en_entries)} en")
    for i, (slug, display, _, _) in enumerate(entries[:5]):
        print(f"        [{i+1}] {display!r:36s} -> {slug}  (+ {slug}.html)")

    bad = []
    for p in DIST_DIR.rglob("*"):
        if p.is_file():
            try:
                p.name.encode("ascii")
            except UnicodeEncodeError:
                bad.append(str(p.relative_to(DIST_DIR)))
    if bad:
        print(f"[diag] WARNING: {len(bad)} non-ASCII filename(s) in dist/")
    else:
        print(f"[diag] OK: all {sum(1 for _ in DIST_DIR.rglob('*') if _.is_file())} files in dist/ are ASCII-safe")

    print(f"[ok] Build complete. {len(entries)} papers, {page_count} HTML pages -> {DIST_DIR}")


# ========== 每篇 HTML 可引用頁 ==========

def write_paper_pages(entries, dist_papers: Path) -> int:
    count = 0
    for slug, display, ext, src in entries:
        body, mode = extract_body(src, ext)
        raw_href = quote(slug)                         # 原檔（同目錄）
        page_url = f"{SITE_URL}/papers/{quote(slug)}.html"

        if mode in ("full", "source") and body:
            note = "" if mode == "full" else '<p style="opacity:0.6">[原始碼檢視 / source view]</p>'
            content = note + body
        else:                                          # landing（pdf 或抽取失敗）
            if ext == "pdf":
                content = (
                    f'<p>PDF 文件。<a href="{raw_href}" target="_blank" rel="noopener">開啟 / 下載原檔</a></p>'
                    f'<iframe src="{raw_href}" style="width:100%;height:80vh;border:1px solid #0f0;margin-top:12px"></iframe>'
                )
            else:
                content = f'<p>原檔：<a href="{raw_href}" target="_blank" rel="noopener">下載 {esc(ext)}</a></p>'

        jsonld = (
            "{\n"
            '  "@context": "https://schema.org",\n'
            '  "@type": "ScholarlyArticle",\n'
            f'  "name": {json_safe(display)},\n'
            f'  "url": "{page_url}",\n'
            f'  "inLanguage": "{lang_tag(display)}",\n'
            f'  "author": {{"@type": "Person", "name": {json_safe(SITE_AUTHOR)}}},\n'
            f'  "publisher": {{"@type": "Organization", "name": {json_safe(SITE_ORG)}}},\n'
            f'  "isPartOf": {{"@type": "Collection", "name": {json_safe(SITE_TITLE)}, "url": "{SITE_URL}"}},\n'
            '  "encodingFormat": "text/html"\n'
            "}"
        )

        doc = (
            "<!DOCTYPE html>\n"
            f'<html lang="{lang_tag(display)}">\n<head>\n'
            '<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            f"<title>{esc(display)} · {esc(SITE_TITLE)}</title>\n"
            f'<meta name="description" content="{esc(display)} — {esc(SITE_TAGLINE)}">\n'
            f'<meta name="author" content="{esc(SITE_AUTHOR)}">\n'
            '<meta name="robots" content="index, follow">\n'
            '<meta name="ai-content-policy" content="indexable, citable, training-allowed">\n'
            f'<link rel="alternate" type="{mime_for(ext)}" href="{raw_href}" title="原始檔 / source ({esc(ext)})">\n'
            f'<link rel="canonical" href="{page_url}">\n'
            f'<script type="application/ld+json">\n{jsonld}\n</script>\n'
            f"<style>{PAGE_CSS}</style>\n</head>\n<body>\n"
            '<div class="nav"><a href="../index.html">&larr; 回 Logic Matrix 索引</a></div>\n'
            f'<header class="header"><h1>{esc(display)}</h1>'
            f'<p>{esc(SITE_TITLE)} · {esc(SITE_ORG)}</p></header>\n'
            f"{disclaimer_html()}\n"
            f"<article>\n{content}\n"
            f'<div class="altbar">原始檔（供 RAG/下載）：'
            f'<a href="{raw_href}" rel="noopener">papers/{esc(slug)}</a> [{esc(ext)}]</div>\n'
            "</article>\n"
            f"<footer><p>{esc(SITE_AUTHOR)} · Cl + ε</p></footer>\n"
            "</body>\n</html>\n"
        )
        (dist_papers / f"{slug}.html").write_text(doc, encoding="utf-8")
        count += 1
    return count


# ========== HTML / 結構化資料（索引）==========

def write_index(zh_entries, en_entries) -> None:
    def render_items(group):
        return "\n".join(
            f'        <li class="paper-item" data-format="{esc(ext)}" data-lang="{lang_tag(display)}">'
            f'<a href="papers/{quote(slug)}.html">'         # ← 改連 HTML 可引用頁
            f'<span class="paper-title">{esc(display)}</span>'
            f'<span class="paper-format">[{esc(ext)}] '
            f'<a href="papers/{quote(slug)}" rel="noopener" style="opacity:0.6">原檔</a></span>'
            f'</a></li>'
            for slug, display, ext, _ in group
        )

    has_any = bool(zh_entries or en_entries)
    if has_any:
        sections = []
        if zh_entries:
            sections.append(
                '      <div class="lang-group lang-zh">\n'
                f'        <h2 class="lang-label">中文 / Chinese ({len(zh_entries)})</h2>\n'
                '        <ul class="paper-list">\n'
                f'{render_items(zh_entries)}\n'
                '        </ul>\n'
                '      </div>'
            )
        if zh_entries and en_entries:
            sections.append('      <hr class="lang-divider">')
        if en_entries:
            sections.append(
                '      <div class="lang-group lang-en">\n'
                f'        <h2 class="lang-label">English ({len(en_entries)})</h2>\n'
                '        <ul class="paper-list">\n'
                f'{render_items(en_entries)}\n'
                '        </ul>\n'
                '      </div>'
            )
        body_html = "\n".join(sections)
    else:
        body_html = (
            '      <ul class="paper-list">'
            '<li class="paper-item">No papers found. Upload supported files (docx/md/pdf/tex/ipynb) to papers/.</li>'
            '</ul>'
        )

    all_entries = list(zh_entries) + list(en_entries)
    parts = []
    for slug, display, ext, _ in all_entries:
        parts.append(
            "    {"
            f'"@type": "ScholarlyArticle", '
            f'"name": {json_safe(display)}, '
            f'"url": "{SITE_URL}/papers/{quote(slug)}.html", '   # ← 正規可引用 URL
            f'"inLanguage": "{lang_tag(display)}", '
            f'"author": {{"@type": "Person", "name": {json_safe(SITE_AUTHOR)}}}, '
            f'"publisher": {{"@type": "Organization", "name": {json_safe(SITE_ORG)}}}, '
            f'"encodingFormat": "text/html"'
            "}"
        )
    jsonld_items = ",\n".join(parts)
    jsonld = (
        "{\n"
        '  "@context": "https://schema.org",\n'
        '  "@type": "Collection",\n'
        f'  "name": {json_safe(f"{SITE_TITLE} {SITE_VERSION}")},\n'
        f'  "description": {json_safe(SITE_TAGLINE)},\n'
        f'  "url": "{SITE_URL}",\n'
        f'  "creator": {{"@type": "Person", "name": {json_safe(SITE_AUTHOR)}}},\n'
        f'  "publisher": {{"@type": "Organization", "name": {json_safe(SITE_ORG)}}},\n'
        '  "hasPart": [\n'
        f'{jsonld_items}\n'
        '  ]\n'
        "}"
    )

    doc = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(SITE_TITLE)} {esc(SITE_VERSION)}</title>
<meta name="description" content="EveMissLab 理論語料庫接入點 — 跨領域整合理論的開放發表平台。">
<meta name="author" content="{esc(SITE_AUTHOR)}">
<meta name="robots" content="index, follow">

<meta property="og:type" content="website">
<meta property="og:title" content="{esc(SITE_TITLE)} {esc(SITE_VERSION)}">
<meta property="og:description" content="{esc(SITE_TAGLINE)}">
<meta property="og:url" content="{SITE_URL}">

<!-- AIO Hint -->
<meta name="ai-content-policy" content="indexable, citable, training-allowed">

<!-- Structured Data for LLM / Search Engine -->
<script type="application/ld+json">
{jsonld}
</script>

<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
      background: #000; color: #0f0;
      font-family: 'Courier New', monospace;
      padding: 20px; line-height: 1.6;
  }}
  .header {{
      text-align: center; border: 2px solid #0f0;
      padding: 20px; margin-bottom: 30px;
  }}
  .header h1 {{ font-size: 2em; letter-spacing: 3px; }}
  .header p  {{ margin-top: 8px; opacity: 0.85; }}
  .disclaimer {{
      border: 1px dashed #ff9900; color: #ff9900;
      padding: 18px; margin: 0 auto 30px; max-width: 1200px;
  }}
  .disclaimer-title {{ font-weight: bold; margin-bottom: 12px; display: block; letter-spacing: 1px; }}
  .disclaimer-block p {{ margin-bottom: 6px; }}
  .disclaimer-divider {{
      border: none; border-top: 1px dashed #ff9900;
      margin: 16px 0; opacity: 0.55;
  }}
  .matrix {{ max-width: 1200px; margin: 0 auto; }}
  .lang-group {{ margin-bottom: 20px; }}
  .lang-label {{
      font-size: 1.1em; letter-spacing: 2px;
      margin-bottom: 12px; padding-bottom: 6px;
      border-bottom: 1px solid #0f0; opacity: 0.85;
  }}
  .lang-divider {{
      border: none; border-top: 1px dashed #0f0;
      margin: 30px 0; opacity: 0.45;
  }}
  .paper-list {{ list-style: none; }}
  .paper-item {{ padding: 8px 0; border-bottom: 1px solid #0f0; }}
  .paper-item a {{
      color: #0f0; text-decoration: none;
      display: flex; justify-content: space-between; gap: 16px;
      transition: all 0.2s;
  }}
  .paper-item a:hover {{
      background: #0f0; color: #000; padding-left: 10px;
  }}
  .paper-format {{ opacity: 0.6; font-size: 0.9em; white-space: nowrap; }}
  footer {{
      max-width: 1200px; margin: 40px auto 0;
      text-align: center; opacity: 0.55; font-size: 0.85em;
  }}
</style>
</head>
<body>
<header class="header">
  <h1>EVEMISSLAB_LOGIC_MATRIX_{esc(SITE_VERSION)}</h1>
  <p>{esc(SITE_TAGLINE)} | NODES: {len(zh_entries) + len(en_entries)} ({len(zh_entries)} ZH / {len(en_entries)} EN)</p>
</header>

{disclaimer_html()}

<main class="matrix">
{body_html}
</main>

<footer>
  <p>{esc(SITE_ORG)} · {esc(SITE_AUTHOR)}</p>
  <p>{esc(SITE_VERSION)} · NODES {len(zh_entries) + len(en_entries)}</p>
</footer>
</body>
</html>
"""
    (DIST_DIR / "index.html").write_text(doc, encoding="utf-8")


def write_robots() -> None:
    body = f"""# EVEMISSLAB Logic Matrix — robots.txt
# AIO-oriented: open to indexing and AI ingestion.

User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: CCBot
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    (DIST_DIR / "robots.txt").write_text(body, encoding="utf-8")


def write_llms_txt(zh_entries, en_entries) -> None:
    """llms.txt — language-grouped。連結指向 HTML 可引用頁。"""
    lines = [
        f"# {SITE_TITLE} {SITE_VERSION}",
        "",
        f"> {SITE_TAGLINE}. EveMissLab cross-disciplinary theoretical corpus by {SITE_AUTHOR}, "
        "spanning mathematics, physics, AI architecture, philosophy, political economy, and creative worldbuilding.",
        "",
        "## Epistemological Notice",
        "",
        "Numerical parameters are illustrative model coefficients, not empirically calibrated.",
        "Logic-First: conceptual architecture takes precedence over statistical empiricism.",
        "",
    ]
    if zh_entries:
        lines += [f"## Papers (中文 / Chinese, {len(zh_entries)})", ""]
        for slug, display, ext, _ in zh_entries:
            lines.append(f"- [{display}]({SITE_URL}/papers/{quote(slug)}.html) — {ext.upper()}")
        lines.append("")
    if en_entries:
        lines += [f"## Papers (English, {len(en_entries)})", ""]
        for slug, display, ext, _ in en_entries:
            lines.append(f"- [{display}]({SITE_URL}/papers/{quote(slug)}.html) — {ext.upper()}")
        lines.append("")
    (DIST_DIR / "llms.txt").write_text("\n".join(lines), encoding="utf-8")


def write_sitemap(entries) -> None:
    urls = [f"  <url><loc>{SITE_URL}/</loc></url>"]
    for slug, _, _, _ in entries:
        urls.append(f"  <url><loc>{SITE_URL}/papers/{quote(slug)}.html</loc></url>")
    body = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (DIST_DIR / "sitemap.xml").write_text(body, encoding="utf-8")


if __name__ == "__main__":
    main()
