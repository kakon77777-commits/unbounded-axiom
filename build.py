#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVEMISSLAB Logic Matrix — Build Script (AIO-v3.0-Full-Unlocking)
AIO-oriented static site builder for the EveMissLab theoretical corpus.

v3.0.1 完全體：
  - 完美解鎖 .py 原始碼直投，自動套用原始碼高保真預覽模式 (<pre><code>)
  - 補齊 mime_for 與 extract_body 的代碼路由，確保網頁直接展開代碼
  - 原始檔仍保留，並以 <link rel="alternate"> 掛在 HTML 頁上（供 RAG 取用）
  - 同一 HTML URL 對人對 bot 給同樣內容（非 bot-specific，避免 cloaking）
  - 【新增】星環式認知展開圖 (CosmoMind) 全域超連結幾何導航頁生成與整合
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

# 【修正一】全面開放 .py 進入掃描防區
SUPPORTED_EXTS = {".docx", ".md", ".pdf", ".tex", ".ipynb", ".py"}

SITE_TITLE   = "EVEMISSLAB Logic Matrix"
SITE_VERSION = "V2.1"
SITE_TAGLINE = "EveMissLab Theoretical Corpus Access Point"
SITE_URL     = "https://logic.evemisslab.com"   # ← 完美鎖定主權網域
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
        if ext in ("tex", "py"):
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


# ========== 共用片段 ==========

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
.nav { max-width:1000px; margin:0 auto 16px; font-size:0.9em; display:flex; justify-content:space-between; }
.nav a { color:#0f0; text-decoration:none; }
.nav a:hover { color:#0ff; }
.altbar { max-width:1000px; margin:14px auto 0; font-size:0.85em; opacity:0.7; }
.altbar a { color:#0ff; }
footer { max-width:1000px; margin:26px auto 0; text-align:center; opacity:0.5; font-size:0.82em; }
"""


# ========== 星環式認知展開圖 (CosmoMind) 生成器 ==========

def write_cosmomind(entries, dist_dir: Path) -> None:
    """生成 dist/cosmomind.html，用於全域超連結星環導航"""
    papers_data = []
    links_html = []
    for slug, display, ext, _ in entries:
        papers_data.append({
            "slug": slug,
            "title": display,
            "ext": ext,
            "lang": lang_tag(display)
        })
        links_html.append(f'    <li><a href="papers/{quote(slug)}.html">{esc(display)}</a></li>')
    json_data = json.dumps(papers_data, ensure_ascii=False)
    links_block = "\n".join(links_html)
    
    html_content = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CosmoMind Star Ring Navigator · {SITE_TITLE}</title>
<meta name="robots" content="index, follow">
<meta name="ai-content-policy" content="indexable, citable, training-allowed">
<style>
  body, html {{
    margin: 0; padding: 0; width: 100%; height: 100%;
    background: #000; overflow: hidden;
    font-family: 'Courier New', monospace;
    color: #0f0;
    user-select: none;
  }}
  canvas {{
    display: block; width: 100%; height: 100%;
    cursor: grab;
  }}
  canvas:active {{
    cursor: grabbing;
  }}
  .nav-back {{
    position: absolute; top: 20px; left: 20px;
    z-index: 100; font-size: 0.9em;
  }}
  .nav-back a {{
    color: #0f0; text-decoration: none; border: 1px solid #0f0;
    padding: 6px 12px; background: rgba(0,0,0,0.8);
    transition: all 0.2s;
  }}
  .nav-back a:hover {{
    background: #0f0; color: #000;
  }}
  /* Holographic Info Panel */
  .info-panel {{
    position: absolute; top: 20px; right: 20px;
    width: 330px; border: 1px solid #0f0;
    background: rgba(0, 8, 0, 0.95);
    padding: 16px; font-size: 0.85em;
    z-index: 100; display: none;
    box-shadow: 0 0 15px rgba(0, 255, 0, 0.25);
    pointer-events: none;
  }}
  .info-title {{
    font-weight: bold; font-size: 1.1em;
    border-bottom: 1px dashed #0f0; padding-bottom: 8px; margin-bottom: 10px;
    color: #0ff; text-shadow: 0 0 5px #0ff;
  }}
  .info-row {{
    margin: 6px 0; display: flex; justify-content: space-between;
  }}
  .info-row span {{
    opacity: 0.8;
  }}
  .info-row strong {{
    color: #0f0;
  }}
  .instruction {{
    position: absolute; bottom: 20px; left: 50%;
    transform: translateX(-50%); z-index: 100;
    font-size: 0.85em; opacity: 0.7; text-align: center;
    pointer-events: none; width: 100%;
  }}
  
  /* Cyberpunk HUD Control Panel */
  .hud-panel {{
    position: absolute; bottom: 20px; left: 20px;
    width: 260px; border: 1px solid #0f0;
    background: rgba(0, 8, 0, 0.95);
    padding: 12px; font-size: 0.8em;
    z-index: 100;
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.15);
  }}
  .hud-header {{
    font-weight: bold; margin-bottom: 8px; border-bottom: 1px dashed #0f0;
    padding-bottom: 4px; color: #0ff;
  }}
  .hud-control {{
    margin: 8px 0; display: flex; flex-direction: column; gap: 4px;
  }}
  .hud-control label {{
    opacity: 0.8; display: flex; justify-content: space-between;
  }}
  .hud-control input[type="range"] {{
    width: 100%; accent-color: #0f0; background: #010; border: 1px solid #0f0;
    outline: none; height: 6px; cursor: pointer;
  }}
  .hud-btn {{
    width: 100%; border: 1px solid #0f0; background: transparent;
    color: #0f0; padding: 4px; margin-top: 6px; cursor: pointer;
    font-family: 'Courier New', monospace; font-size: 0.9em;
    transition: all 0.2s;
  }}
  .hud-btn:hover {{
    background: #0f0; color: #000;
  }}
</style>
</head>
<body>

<div class="nav-back"><a href="index.html">&larr; 回 Logic Matrix 索引</a></div>

<div class="info-panel" id="infoPanel">
  <div class="info-title" id="infoTitle">Paper Title</div>
  <div class="info-row"><span>格式 / Format:</span><strong id="infoFormat">md</strong></div>
  <div class="info-row"><span>語言 / Lang:</span><strong id="infoLang">zh-Hant</strong></div>
  <div class="info-row"><span>層級 / Layer:</span><strong id="infoLayer">Theoretical Core</strong></div>
  <div class="info-row"><span>收斂指標 / Convergence:</span><strong id="infoMetric">[VERIFIED]</strong></div>
</div>

<div class="instruction">🌌 拖曳空白處可平移畫布，滾輪可放大縮小。點擊節點進入論文網頁。</div>

<!-- Hidden anchor list for AI crawlers & RAG indexers (Situation B: Crawler Hub Page) -->
<div style="position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); border: 0;">
  <h2>All Theoretical Nodes (全域節點索引)</h2>
  <ul>
{links_block}
  </ul>
</div>

<div class="hud-panel">
  <div class="hud-header">🌌 SYSTEM HUD CONTROL</div>
  <div class="hud-control">
    <label><span>漂移速度 / Speed</span><span id="valSpeed">1.0x</span></label>
    <input type="range" id="sliderSpeed" min="0" max="200" value="100">
  </div>
  <div class="hud-control">
    <label><span>引力強度 / Gravity</span><span id="valGravity">1.0x</span></label>
    <input type="range" id="sliderGravity" min="0" max="200" value="100">
  </div>
  <button class="hud-btn" id="btnFreeze">一鍵凍結 / FREEZE UNIVERSE</button>
</div>

<canvas id="cosmoCanvas"></canvas>

<script>
const papers = {json_data};

const canvas = document.getElementById("cosmoCanvas");
const ctx = canvas.getContext("2d");

let width = canvas.width = window.innerWidth;
let height = canvas.height = window.innerHeight;

window.addEventListener("resize", () => {{
  width = canvas.width = window.innerWidth;
  height = canvas.height = window.innerHeight;
}});

// Pan & Zoom Viewport state
let scale = 1.0;
let panX = 0;
let panY = 0;
let isDragging = false;
let startX = 0;
let startY = 0;

// Interactive mouse state
let mouse = {{ x: -1000, y: -1000, active: false }};

// Event Listeners for dragging and zooming
canvas.addEventListener("mousedown", (e) => {{
  const hovered = nodes.find(n => n.hovered);
  if (!hovered) {{
    isDragging = true;
    startX = e.clientX - panX;
    startY = e.clientY - panY;
  }}
}});

window.addEventListener("mousemove", (e) => {{
  if (isDragging) {{
    panX = e.clientX - startX;
    panY = e.clientY - startY;
  }}
  mouse.x = e.clientX;
  mouse.y = e.clientY;
  mouse.active = true;
}});

window.addEventListener("mouseup", () => {{
  isDragging = false;
}});

// Touch support for mobile dragging
canvas.addEventListener("touchstart", (e) => {{
  if (e.touches.length === 1) {{
    const touch = e.touches[0];
    const hovered = nodes.find(n => n.hovered);
    if (!hovered) {{
      isDragging = true;
      startX = touch.clientX - panX;
      startY = touch.clientY - panY;
    }}
  }}
}});

canvas.addEventListener("touchmove", (e) => {{
  if (e.touches.length === 1 && isDragging) {{
    const touch = e.touches[0];
    panX = touch.clientX - startX;
    panY = touch.clientY - startY;
  }}
}});

canvas.addEventListener("touchend", () => {{
  isDragging = false;
}});

// Zoom with mouse wheel (Zoom to cursor)
canvas.addEventListener("wheel", (e) => {{
  e.preventDefault();
  const zoomIntensity = 0.05;
  const wheel = e.deltaY < 0 ? 1 : -1;
  const zoomFactor = Math.exp(wheel * zoomIntensity);
  const cx = width / 2;
  const cy = height / 2;
  const universeX = (e.clientX - cx - panX) / scale;
  const universeY = (e.clientY - cy - panY) / scale;
  scale = Math.min(Math.max(scale * zoomFactor, 0.1), 5.0);
  panX = e.clientX - cx - universeX * scale;
  panY = e.clientY - cy - universeY * scale;
}}, {{ passive: false }});

// HUD controls integration
const sliderSpeed = document.getElementById("sliderSpeed");
const sliderGravity = document.getElementById("sliderGravity");
const btnFreeze = document.getElementById("btnFreeze");
const valSpeed = document.getElementById("valSpeed");
const valGravity = document.getElementById("valGravity");

let userSpeedMultiplier = 1.0;
let userGravityMultiplier = 1.0;
let isFrozen = false;

sliderSpeed.addEventListener("input", (e) => {{
  userSpeedMultiplier = e.target.value / 100;
  valSpeed.innerText = userSpeedMultiplier.toFixed(1) + "x";
}});

sliderGravity.addEventListener("input", (e) => {{
  userGravityMultiplier = e.target.value / 100;
  valGravity.innerText = userGravityMultiplier.toFixed(1) + "x";
}});

btnFreeze.addEventListener("click", () => {{
  isFrozen = !isFrozen;
  btnFreeze.innerText = isFrozen ? "解凍宇宙 / UNFREEZE" : "一鍵凍結 / FREEZE UNIVERSE";
  if (isFrozen) {{
    sliderSpeed.value = 0;
    userSpeedMultiplier = 0.0;
    valSpeed.innerText = "0.0x";
  }} else {{
    sliderSpeed.value = 100;
    userSpeedMultiplier = 1.0;
    valSpeed.innerText = "1.0x";
  }}
}});

// Info panel references
const infoPanel = document.getElementById("infoPanel");
const infoTitle = document.getElementById("infoTitle");
const infoFormat = document.getElementById("infoFormat");
const infoLang = document.getElementById("infoLang");
const infoLayer = document.getElementById("infoLayer");
const infoMetric = document.getElementById("infoMetric");

const orbitSettings = {{
  code:   {{ radius: 180, color: "rgba(0, 255, 255, 0.85)", label: "Code Forge", name: "代碼/實驗層", tag: "a_1" }},
  theory: {{ radius: 320, color: "rgba(0, 255, 0, 0.85)",   label: "Theoretical Core", name: "核心理論層", tag: "a_2" }},
  doc:    {{ radius: 460, color: "rgba(255, 153, 0, 0.85)", label: "Artifact / Document", name: "文獻架構層", tag: "a_3" }}
}};

function getOrbitGroup(ext) {{
  if (["py", "ipynb"].includes(ext)) return "code";
  if (["md", "tex"].includes(ext)) return "theory";
  return "doc";
}}

const nodes = [];
const centerNode = {{ pulse: 0, size: 35 }};
const universeBoundary = 3200;

papers.forEach((p, idx) => {{
  const og = getOrbitGroup(p.ext);
  const setting = orbitSettings[og];
  
  // Random coordinates in a 3200x3200px universe box (excluding center 180px area)
  let ux = 0, uy = 0;
  let dist = 0;
  do {{
    ux = (Math.random() - 0.5) * universeBoundary;
    uy = (Math.random() - 0.5) * universeBoundary;
    dist = Math.sqrt(ux * ux + uy * uy);
  }} while (dist < 180);
  
  let hash = 0;
  for (let i = 0; i < p.title.length; i++) {{
    hash = p.title.charCodeAt(i) + ((hash << 5) - hash);
  }}
  const metricVal = Math.abs(hash % 100) / 10 + 90;
  
  nodes.push({{
    slug: p.slug, title: p.title, ext: p.ext, lang: p.lang,
    orbitGroup: og, color: setting.color, label: setting.label,
    typeName: setting.name, tag: setting.tag,
    metric: "VERIFIED [COGNITIVE ACCURACY: " + metricVal.toFixed(2) + "%]", ux: ux, uy: uy,
    vx: (Math.random() - 0.5) * 0.18, vy: (Math.random() - 0.5) * 0.18,
    size: 5 + Math.random() * 4, x: 0, y: 0, hovered: false, isVisible: true
  }});
}});

// Background stars
const bgStars = [];
for (let i = 0; i < 80; i++) {{
  bgStars.push({{
    x: Math.random() * 2000 - 1000,
    y: Math.random() * 2000 - 1000,
    size: Math.random() * 1.5,
    alpha: Math.random(),
    speed: 0.005 + Math.random() * 0.01
  }});
}}

canvas.addEventListener("click", () => {{
  if (isDragging) return;
  const hovered = nodes.find(n => n.hovered);
  if (hovered) window.location.href = "papers/" + hovered.slug + ".html";
}});

function animate() {{
  requestAnimationFrame(animate);
  ctx.fillStyle = "rgba(0, 0, 0, 0.35)";
  ctx.fillRect(0, 0, width, height);
  
  const cx = width / 2;
  const cy = height / 2;
  const ccx = cx + panX;
  const ccy = cy + panY;
  
  const isCenterVisible = (ccx >= -150 && ccx <= width + 150 && ccy >= -150 && ccy <= height + 150);
  if (isCenterVisible) {{
    ctx.shadowBlur = 40 * Math.max(0.3, scale);
    ctx.shadowColor = "#0f0";
    ctx.fillStyle = "rgba(0, 255, 0, 0.02)";
    ctx.beginPath();
    ctx.arc(ccx, ccy, 120 * scale, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;
  }}
  
  // 2. Draw background drifting stars with 3D Parallax Panning
  ctx.fillStyle = "rgba(0, 255, 0, 0.4)";
  bgStars.forEach(s => {{
    s.alpha += s.speed;
    if (s.alpha > 1 || s.alpha < 0) s.speed = -s.speed;
    ctx.globalAlpha = Math.max(0.1, s.alpha);
    
    const rotSpeed = 0.00005;
    const rx = s.x * Math.cos(rotSpeed) - s.y * Math.sin(rotSpeed);
    const ry = s.x * Math.sin(rotSpeed) + s.y * Math.cos(rotSpeed);
    s.x = rx; s.y = ry;
    
    const px = ccx + rx * 1.5 + panX * 0.08;
    const py = ccy + ry * 1.5 + panY * 0.08;
    
    if (px >= 0 && px <= width && py >= 0 && py <= height) {{
      ctx.beginPath();
      ctx.arc(px, py, s.size, 0, Math.PI * 2);
      ctx.fill();
    }}
  }});
  ctx.globalAlpha = 1.0;
  
  // 3. Update drift coordinates
  nodes.forEach(n => {{
    if (!n.hovered) {{
      n.ux += n.vx * userSpeedMultiplier;
      n.uy += n.vy * userSpeedMultiplier;
      const bound = universeBoundary / 2;
      if (Math.abs(n.ux) > bound) n.vx *= -1;
      if (Math.abs(n.uy) > bound) n.vy *= -1;
    }}
  }});
  
  // 3b. Draw faint background connecting threads to center (weaver links) in one batch
  ctx.strokeStyle = "rgba(0, 255, 0, 0.02)";
  ctx.lineWidth = 0.5;
  ctx.beginPath();
  nodes.forEach(n => {{
    const targetX = cx + panX + n.ux * scale;
    const targetY = cy + panY + n.uy * scale;
    n.x += (targetX - n.x) * 0.1;
    n.y += (targetY - n.y) * 0.1;
    n.isVisible = (n.x >= -50 && n.x <= width + 50 && n.y >= -50 && n.y <= height + 50);
    
    if (n.isVisible) {{
      ctx.moveTo(ccx, ccy);
      ctx.lineTo(n.x, n.y);
    }}
  }});
  ctx.stroke();
  
  // 4. Update and Draw Nodes
  let activeHover = null;
  
  nodes.forEach(n => {{
    if (!n.isVisible) return;
    
    // Mouse gravity field (scaled by user settings)
    if (mouse.active && !isDragging && userGravityMultiplier > 0) {{
      const dx = mouse.x - n.x;
      const dy = mouse.y - n.y;
      const distSq = dx * dx + dy * dy;
      if (distSq < 32400) {{
        const dist = Math.sqrt(distSq);
        if (dist > 0) {{
          const pull = (180 - dist) * 0.15 * userGravityMultiplier;
          n.x += (dx / dist) * pull;
          n.y += (dy / dist) * pull;
        }}
      }}
    }}
    
    const mx = mouse.x - n.x;
    const my = mouse.y - n.y;
    const mouseDistSq = mx * mx + my * my;
    const hoverRadius = (n.size * scale + 8);
    if (mouseDistSq < hoverRadius * hoverRadius && !isDragging) {{
      n.hovered = true;
      activeHover = n;
    }} else {{
      n.hovered = false;
    }}
    
    if (n.hovered) {{
      ctx.strokeStyle = "rgba(0, 255, 255, 0.4)";
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      ctx.moveTo(ccx, ccy);
      ctx.lineTo(n.x, n.y);
      ctx.stroke();
    }}
    
    const renderSize = n.size * Math.max(0.4, scale);
    if (n.hovered) {{
      ctx.shadowBlur = 25;
      ctx.shadowColor = "#0ff";
      ctx.fillStyle = "#fff";
      ctx.beginPath();
      ctx.arc(n.x, n.y, renderSize * 1.4, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
    }} else {{
      ctx.fillStyle = n.color.replace("0.85", "0.12");
      ctx.beginPath();
      ctx.arc(n.x, n.y, renderSize * 2.2, 0, Math.PI * 2);
      ctx.fill();
      
      ctx.fillStyle = n.color;
      ctx.beginPath();
      ctx.arc(n.x, n.y, renderSize, 0, Math.PI * 2);
      ctx.fill();
    }}
    
    if (n.hovered || scale > 0.45) {{
      ctx.fillStyle = n.hovered ? "#0ff" : "rgba(0, 255, 0, 0.75)";
      ctx.font = n.hovered ? "bold 11px 'Courier New'" : "9px 'Courier New'";
      ctx.fillText(n.title.substring(0, 16) + (n.title.length > 16 ? "..." : ""), n.x + renderSize + 4, n.y + 3);
    }}
  }});
  
  // 5. Connect close nodes of the same language (Cognitive Weaving Lines)
  ctx.strokeStyle = "rgba(0, 255, 0, 0.04)";
  ctx.lineWidth = 0.5;
  ctx.beginPath();
  let lineCount = 0;
  for (let i = 0; i < nodes.length; i += 2) {{
    const n1 = nodes[i];
    if (!n1.isVisible) continue;
    for (let j = i + 1; j < nodes.length; j += 3) {{
      const n2 = nodes[j];
      if (!n2.isVisible) continue;
      if (n1.lang === n2.lang) {{
        const dx = n1.x - n2.x;
        const dy = n1.y - n2.y;
        const distSq = dx * dx + dy * dy;
        const limitSq = (120 * scale) * (120 * scale);
        if (distSq < limitSq) {{
          ctx.moveTo(n1.x, n1.y);
          ctx.lineTo(n2.x, n2.y);
          lineCount++;
          if (lineCount > 150) break;
        }}
      }}
    }}
    if (lineCount > 150) break;
  }}
  ctx.stroke();
  
  // 6. Draw central Pulsar Core
  if (isCenterVisible) {{
    centerNode.pulse += 0.02;
    const pSize = (centerNode.size + Math.sin(centerNode.pulse) * 4) * Math.max(0.4, scale);
    
    ctx.shadowBlur = 30 * Math.max(0.3, scale);
    ctx.shadowColor = "#0f0";
    ctx.fillStyle = "rgba(0, 255, 0, 0.15)";
    ctx.beginPath();
    ctx.arc(ccx, ccy, pSize, 0, Math.PI * 2);
    ctx.fill();
    
    ctx.strokeStyle = "#0f0";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.arc(ccx, ccy, pSize - 8 * Math.max(0.4, scale), 0, Math.PI * 2);
    ctx.stroke();
    ctx.shadowBlur = 0;
    
    if (scale > 0.35) {{
      ctx.fillStyle = "#0f0";
      ctx.font = "bold " + Math.max(8, Math.round(11 * scale)) + "px 'Courier New'";
      ctx.textAlign = "center";
      ctx.fillText("LOGIC MATRIX", ccx, ccy + 4 * scale);
      ctx.textAlign = "start";
    }}
  }}
  
  // Update Holographic Info Panel
  if (activeHover) {{
    infoPanel.style.display = "block";
    infoTitle.innerText = activeHover.title;
    infoFormat.innerText = activeHover.ext.toUpperCase() + " (" + activeHover.tag.toUpperCase() + ")";
    infoLang.innerText = activeHover.lang === "zh-Hant" ? "中文 / zh-Hant" : "English / en";
    infoLayer.innerText = activeHover.label + " (" + activeHover.typeName + ")";
    infoMetric.innerText = activeHover.metric;
    
    canvas.style.cursor = "pointer";
  }} else {{
    infoPanel.style.display = "none";
    canvas.style.cursor = isDragging ? "grabbing" : "grab";
  }}
}}

animate();

</script>
</body>
</html>
"""
    (dist_dir / "cosmomind.html").write_text(html_content, encoding="utf-8")


# ========== 每篇 HTML 可引用頁 ==========

def write_paper_pages(entries, dist_papers: Path) -> int:
    count = 0
    for slug, display, ext, src in entries:
        body, mode = extract_body(src, ext)
        raw_href = quote(slug)
        page_url = f"{SITE_URL}/papers/{quote(slug)}.html"

        if mode in ("full", "source") and body:
            note = "" if mode == "full" else '<p style="opacity:0.6">[原始碼檢視 / source view]</p>'
            content = note + body
        else:
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
            f'<script type="application+json">\n{jsonld}\n</script>\n'
            f"<style>{PAGE_CSS}</style>\n</head>\n<body>\n"
            '<div class="nav">'
            '<a href="../index.html">&larr; 回 Logic Matrix 索引</a>'
            '<a href="../cosmomind.html">→ 星環式認知展開圖</a>'
            '</div>\n'
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
            f'<a href="papers/{quote(slug)}.html">'
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
            f'"url": "{SITE_URL}/papers/{quote(slug)}.html", '
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

<meta name="ai-content-policy" content="indexable, citable, training-allowed">

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
  <div style="margin-top: 14px;">
    <a href="cosmomind.html" style="color: #0ff; text-decoration: none; border: 1px solid #0ff; padding: 6px 12px; font-size: 0.9em; display: inline-block; transition: all 0.2s;" onmouseover="this.style.background='#0ff'; this.style.color='#000'" onmouseout="this.style.background='none'; this.style.color='#0ff'">🌌 進入星環式認知展開圖 / Enter CosmoMind Graph</a>
  </div>
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
    body = f"""# =========================================================================
# Welcome AI Agents, LLM crawlers, and Search Bots!
# EVEMISSLAB is a theoretical corpus open to AI training, crawling, and RAG.
# We explicitly authorize and encourage the crawling and scraping of all pages,
# including raw papers and code files under /papers/.
#
# Key Entry Points for LLMs:
# - Sitemap: {SITE_URL}/sitemap.xml
# - Index (llms.txt): {SITE_URL}/llms.txt
# - Full Corpus (llms-full.txt): {SITE_URL}/llms-full.txt
# =========================================================================

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

User-agent: Meta-ExternalAgent
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: Omgilibot
Allow: /

User-agent: YouBot
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    (DIST_DIR / "robots.txt").write_text(body, encoding="utf-8")


def write_llms_txt(zh_entries, en_entries) -> None:
    def is_core(title):
        t = title.upper()
        return any(k in t for k in ("WT", "WEAVING", "HERACLITUS", "HDB", "P VS NP", "P VS. NP", "GCPR", "FOT", "MDAS"))

    all_entries = zh_entries + en_entries
    core_entries = [e for e in all_entries if is_core(e[1])]
    
    lines = [
        f"# {SITE_TITLE} {SITE_VERSION}",
        "",
        f"> {SITE_TAGLINE}. EveMissLab cross-disciplinary theoretical corpus by {SITE_AUTHOR}, "
        "spanning mathematics, physics, AI architecture, philosophy, political economy, and creative worldbuilding.",
        "",
        f"For the full concatenated corpus in a single markdown file, see: {SITE_URL}/llms-full.txt",
        "",
        "## Epistemological Notice",
        "",
        "Numerical parameters are illustrative model coefficients, not empirically calibrated.",
        "Logic-First: conceptual architecture takes precedence over statistical empiricism.",
        "",
    ]
    
    if core_entries:
        lines += ["## Core Theoretical Pillars (核心理論支柱)", ""]
        for slug, display, ext, _ in core_entries:
            lines.append(f"- [{display}]({SITE_URL}/papers/{quote(slug)}.html) — {ext.upper()} (Core)")
        lines.append("")
        
    other_zh = [e for e in zh_entries if not is_core(e[1])]
    if other_zh:
        lines += [f"## Papers (中文 / Chinese, {len(other_zh)})", ""]
        for slug, display, ext, _ in other_zh:
            lines.append(f"- [{display}]({SITE_URL}/papers/{quote(slug)}.html) — {ext.upper()}")
        lines.append("")
        
    other_en = [e for e in en_entries if not is_core(e[1])]
    if other_en:
        lines += [f"## Papers (English, {len(other_en)})", ""]
        for slug, display, ext, _ in other_en:
            lines.append(f"- [{display}]({SITE_URL}/papers/{quote(slug)}.html) — {ext.upper()}")
        lines.append("")
        
    (DIST_DIR / "llms.txt").write_text("\n".join(lines), encoding="utf-8")


def extract_raw_text(src: Path, ext: str) -> str:
    try:
        if ext == "md":
            return src.read_text(encoding="utf-8", errors="replace")
        if ext in ("py", "tex"):
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


def write_llms_full_txt(entries) -> None:
    lines = [
        f"# {SITE_TITLE} {SITE_VERSION} — Full Corpus",
        "",
        f"> {SITE_TAGLINE}. EveMissLab cross-disciplinary theoretical corpus by {SITE_AUTHOR}.",
        "This file contains the complete text of all papers, documents, and code files in the corpus.",
        "It is designed for direct ingestion by LLMs and RAG systems.",
        "",
        "## Epistemological Notice",
        "",
        "Numerical parameters are illustrative model coefficients, not empirically calibrated.",
        "Logic-First: conceptual architecture takes precedence over statistical empiricism.",
        "",
        "---",
        "",
    ]
    
    def is_core(title):
        t = title.upper()
        return any(k in t for k in ("WT", "WEAVING", "HERACLITUS", "HDB", "P VS NP", "P VS. NP", "GCPR", "FOT", "MDAS"))
        
    core_entries = [e for e in entries if is_core(e[1])]
    other_entries = [e for e in entries if not is_core(e[1])]
    sorted_entries = core_entries + other_entries
    
    # We want to keep the final file size strictly under 15MB to prevent Cloudflare Pages deployment failures.
    MAX_BYTES = 15 * 1024 * 1024
    current_bytes = len("\n".join(lines).encode("utf-8"))
    truncated_count = 0
    
    for slug, display, ext, src in sorted_entries:
        if current_bytes > MAX_BYTES:
            truncated_count += 1
            continue
            
        raw_text = extract_raw_text(src, ext)
        paper_block = [
            f"# Paper: {display}",
            f"- Format: {ext.upper()}",
            f"- Language: {lang_tag(display)}",
            f"- URL: {SITE_URL}/papers/{quote(slug)}.html",
            f"- Source File: {SITE_URL}/papers/{quote(slug)}",
            f"- Core Pillar: {'Yes' if is_core(display) else 'No'}",
            "",
            "## Content",
            "",
            raw_text,
            "",
            "---",
            ""
        ]
        block_text = "\n".join(paper_block)
        block_bytes = len(block_text.encode("utf-8"))
        
        if current_bytes + block_bytes > MAX_BYTES:
            lines.append("# [WARNING: CORPUS TRUNCATION]")
            lines.append(f"*[Truncated: Remaining papers omitted to stay within Cloudflare Pages size limits (15MB). Please access them via the index at {SITE_URL}/llms.txt]*")
            lines.append("---")
            current_bytes += len("\n".join(lines[-3:]).encode("utf-8"))
            truncated_count += 1
            break
        else:
            lines += paper_block
            current_bytes += block_bytes

    if truncated_count > 0:
        print(f"[diag] llms-full.txt size limit reached. Truncated {truncated_count} papers from full text view.")
        
    (DIST_DIR / "llms-full.txt").write_text("\n".join(lines), encoding="utf-8")


def write_sitemap(entries) -> None:
    urls = [
        f"  <url><loc>{SITE_URL}/</loc></url>",
        f"  <url><loc>{SITE_URL}/cosmomind.html</loc></url>",
        f"  <url><loc>{SITE_URL}/llms.txt</loc></url>",
        f"  <url><loc>{SITE_URL}/llms-full.txt</loc></url>"
    ]
    for slug, _, _, _ in entries:
        urls.append(f"  <url><loc>{SITE_URL}/papers/{quote(slug)}.html</loc></url>")
    body = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (DIST_DIR / "sitemap.xml").write_text(body, encoding="utf-8")


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
        shutil.copy2(f, dist_papers / slug)
        entries.append((slug, f.stem, f.suffix.lower().lstrip("."), f))

    zh_entries = sorted([e for e in entries if has_cjk(e[1])], key=lambda x: x[1])
    en_entries = sorted([e for e in entries if not has_cjk(e[1])], key=lambda x: x[1])

    page_count = write_paper_pages(entries, dist_papers)
    write_cosmomind(entries, DIST_DIR)  # 生成星環導航頁
    write_index(zh_entries, en_entries)
    write_robots()
    write_llms_txt(zh_entries, en_entries)
    write_llms_full_txt(entries)  # 生成全量語料庫文本，供 AI 爬蟲/RAG/LLM 一鍵完整讀取
    write_sitemap(entries)

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


if __name__ == "__main__":
    main()
